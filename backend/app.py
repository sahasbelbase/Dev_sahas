from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_marshmallow import Marshmallow
from flask_mysqldb import MySQL
from flask_cors import CORS
from datetime import datetime
from models import db, person, hotel, branch, customer, addressType, address, personAddress, branchAddress, hotelAddress, contactType, contactInformation, personContact, hotelContact, branchContact, roomType, room, booking, serviceType, food, facility, invoice, transaction, payment
from serializers import personSchema, hotelSchema, branchSchema, customerSchema, addressTypeSchema, addressSchema, \
    personAddressSchema, hotelAddressSchema, branchAddressSchema, contactTypeSchema, contactInformationSchema, \
    personContactSchema, hotelContactSchema, branchContactSchema, roomTypeSchema, roomSchema, bookingSchema, \
    serviceTypeSchema, foodSchema, facilitySchema, invoiceSchema, transactionSchema, paymentSchema

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configuration for MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'hrs'

# Set SQLAlchemy URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/hrs'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Marshmallow
db.init_app(app)

# Link SQLAlchemy to Flask app
ma = Marshmallow(app)


# Initialize schema objects
personSchema = personSchema()
hotelSchema = hotelSchema()
branchSchema = branchSchema()
customerSchema = customerSchema()
addressTypeSchema = addressTypeSchema()
addressSchema = addressSchema()
personAddressSchema = personAddressSchema()
hotelAddressSchema = hotelAddressSchema()
branchAddressSchema = branchAddressSchema()
contactTypeSchema = contactTypeSchema()
contactInformationSchema = contactInformationSchema()
personContactSchema = personContactSchema()
hotelContactSchema = hotelContactSchema()
branchContactSchema = branchContactSchema()
roomTypeSchema = roomTypeSchema()
roomSchema = roomSchema()
bookingSchema = bookingSchema()
serviceTypeSchema = serviceTypeSchema()
foodSchema = foodSchema()
facilitySchema = facilitySchema()
invoiceSchema = invoiceSchema()
transactionSchema = transactionSchema()
paymentSchema = paymentSchema()

# API routes
@app.route('/')
def index():
    return 'API'

# Route to get all persons
@app.route('/persons', methods=['GET'])
def getAllPersons():
    persons = person.query.all()
    return jsonify(personSchema.dump(persons, many=True)), 200

# Route to get a specific person by ID
@app.route('/persons/<int:personId>', methods=['GET'])
def getPersonById(personId):
    personObj = person.query.get_or_404(personId)
    return jsonify(personSchema.dump(personObj)), 200

# Route to create a new person
@app.route('/persons', methods=['POST'])
def createPerson():
    data = request.json
    newPerson = person(FullName=data['fullName'], SSN=data['ssn'], Title=data['title'])
    db.session.add(newPerson)
    db.session.commit()
    return jsonify(personSchema.dump(newPerson)), 201

# Route to get all persons with address information
@app.route('/persons', methods=['GET'])
def getAllPersonsWithAddress():
    persons = person.query.all()
    # Include address information
    result = []
    for p in persons:
        person_data = personSchema.dump(p)
        person_data['personAddress'] = personAddressSchema.dump(p.personAddress)  # Assuming person has a personAddress relationship
        result.append(person_data)
    return jsonify(result), 200

# Route to get all address types
@app.route('/addressTypes', methods=['GET'])
def getAllAddressTypes():
    addressTypes = addressType.query.all()
    return jsonify(addressTypeSchema.dump(addressTypes, many=True)), 200

# Route to get all addresses
@app.route('/addresses', methods=['GET'])
def getAllAddresses():
    addresses = address.query.all()
    return jsonify(addressSchema.dump(addresses, many=True)), 200


# Route to get all hotels
@app.route('/hotels', methods=['GET'])
def get_all_hotels():
    hotels = hotel.query.all()
    hotels_data = []

    for h in hotels:
        hotel_data = hotelSchema.dump(h)
        hotel_data['hotelAddress'] = hotelAddressSchema.dump(h.hotelAddress) if h.hotelAddress else None
        hotels_data.append(hotel_data)

    return jsonify(hotels_data), 200

# Route to get all hotels with address information
@app.route('/hotelsWithAddress', methods=['GET'])
def getAllHotelsWithAddress():
    hotels = hotel.query.all()
    result = []

    for h in hotels:
        hotel_data = hotelSchema.dump(h)
        hotel_address = hotelAddress.query.filter_by(hotelId=h.hotelId).first()

        if hotel_address:
            address_data = addressSchema.dump(hotel_address.address)
            hotel_data['hotelAddress'] = address_data
        else:
            hotel_data['hotelAddress'] = None

        result.append(hotel_data)

    return jsonify(result), 200

# Route to create/update a hotel address
@app.route('/hoteladdress', methods=['POST'])
def createOrUpdateHotelAddress():
    data = request.json.get('json')  # Extract the 'json' field from the request data
    hotel_address_data = data.get('hotelAddressData')
    action = data.get('action')

    if action.lower() == 'submit':
        # Assuming 'hotel_address_data' is a dictionary with the necessary information
        new_hotel_address = hotelAddress(
            hotelID=hotel_address_data.get('hotelID'),
            addressID=hotel_address_data.get('addressID')
            # Add other fields as needed
        )

        # Fetch the associated hotel
        hotel = hotel.query.get(hotel_address_data.get('hotelID'))

        if hotel:
            # Associate the new hotel address with the hotel
            hotel.hotelAddress = new_hotel_address
            db.session.add(new_hotel_address)
            db.session.commit()

            result = hotelAddressSchema.dump(new_hotel_address)
            return jsonify(result), 201  # Adjust 'result' based on your actual response
        else:
            return jsonify({'message': 'Hotel not found'}), 404
    else:
        return jsonify({'message': 'Invalid action'}), 400

    


# Route to get all branches with address information
@app.route('/branches', methods=['GET'])
def get_all_branches_with_address():
    branches = branch.query.all()
    result = []
    for b in branches:
        branch_data = branchSchema.dump(b)
        branch_address = branchAddress.query.filter_by(branchId=b.branchId).first()

        if branch_address:
            address_data = addressSchema.dump(branch_address.address)
            branch_data['branchAddress'] = address_data
        else:
            branch_data['branchAddress'] = None

        result.append(branch_data)
    return jsonify(result), 200

# Route to get all branch addresses
@app.route('/branchaddresses', methods=['GET'])
def get_all_branch_addresses():
    branch_addresses = branchAddress.query.all()
    result = [branchAddressSchema.dump(addr) for addr in branch_addresses]
    return jsonify(result), 200

# Route to add a branch
@app.route('/addBranch', methods=['POST'])
def add_branch():
    try:
        data = request.json  # Assuming the data is sent as JSON

        # Extract data from the request
        branch_data = data.get('branchData', {})
        address_data = data.get('addressData', {})

        # Check if required fields are present
        if 'addressTypeId' not in address_data:
            return jsonify({"error": "AddressTypeId is required"}), 400

        # Create a new address
        new_address = address(
            addressTypeId=address_data.get('addressTypeId'),
            country=address_data.get('country'),
            city=address_data.get('city'),
            streetName=address_data.get('streetName'),
            userPersonId=address_data.get('userPersonId')
        )

        db.session.add(new_address)
        db.session.commit()

        # Create a new branch
        new_branch = branch(
            hotelId=branch_data.get('hotelId'),
            name=branch_data.get('name'),
            userPersonId=branch_data.get('userPersonId')
        )

        db.session.add(new_branch)
        db.session.commit()

        # Create a new branchAddress
        new_branch_address = branchAddress(
            branchId=new_branch.branchId,
            addressId=new_address.addressId,
            userPersonId=branch_data.get('userPersonId')
        )

        db.session.add(new_branch_address)
        db.session.commit()

        return jsonify({"message": "Branch added successfully"}), 201

    except Exception as e:
        # Log the error or handle it as needed
        print(f"Error adding branch: {str(e)}")
        return jsonify({"error": "An error occurred while adding the branch"}), 500



# Route to get all customers
@app.route('/customers', methods=['GET'])
def get_all_customers():
    customers = customer.query.all()
    result = []

    for c in customers:
        customer_data = customerSchema.dump(c)
        
        # Get related person data
        person_data = personSchema.dump(c.person)
        
        # Include person details in customer data
        customer_data['fullName'] = person_data['fullName']
        customer_data['ssn'] = person_data['ssn']
        
        # Include address information if available
        person_address = personAddress.query.filter_by(personId=c.personId).first()
        if person_address:
            address_data = addressSchema.dump(person_address.address)
            customer_data['address'] = address_data

        result.append(customer_data)

    return jsonify(result)


# Route to create a new customer
@app.route('/customers', methods=['POST'])
def create_customer():
    try:
        data = request.json

        # Extract person data from the request
        person_data = data.get('person', {})
        
        # Check if 'fullName' is provided and not empty
        if 'fullName' not in person_data or not person_data['fullName']:
            return jsonify({"error": "fullName is required and cannot be empty"}), 400

        # Create a new person
        new_person = person(fullName=person_data['fullName'], SSN=person_data.get('ssn'), Title=person_data.get('title'))
        db.session.add(new_person)
        db.session.commit()        
        data['person'] = new_person
        new_customer = customer(**data)
        db.session.add(new_customer)
        db.session.commit()
        return customerSchema.jsonify(new_customer), 201

    except Exception as e:
        # Log the error or handle it as needed
        print(f"Error creating customer: {str(e)}")
        return jsonify({"error": "An error occurred while creating the customer"}), 500




# Route to get all customers with address information
@app.route('/customers-with-address', methods=['GET'])
def get_all_customers_with_address():
    customers = customer.query.all()
    result = []
    
    for c in customers:
        customer_data = customerSchema.dump(c)
        person_address = personAddress.query.filter_by(personId=c.personId).first()
        
        if person_address:
            address_data = addressSchema.dump(person_address.address)
            customer_data['address'] = address_data
        
        result.append(customer_data)
    
    return jsonify(result)

# Route to get all contact types
@app.route('/contactTypes', methods=['GET'])
def getAllContactTypes():
    contactTypes = contactType.query.all()
    return jsonify(contactTypeSchema.dump(contactTypes, many=True)), 200

# Route to get all contact information
@app.route('/contactInformation', methods=['GET'])
def getAllContactInformation():
    contactInfo = contactInformation.query.all()
    return jsonify(contactInformationSchema.dump(contactInfo, many=True)), 200

# Route to get all person contacts
@app.route('/personContacts', methods=['GET'])
def getAllPersonContacts():
    personContacts = personContact.query.all()
    return jsonify(personContactSchema.dump(personContacts, many=True)), 200

# Route to get all hotel contacts
@app.route('/hotelContacts', methods=['GET'])
def getAllHotelContacts():
    hotelContacts = hotelContact.query.all()
    return jsonify(hotelContactSchema.dump(hotelContacts, many=True)), 200

# Route to get all room types
@app.route('/roomTypes', methods=['GET'])
def getAllRoomTypes():
    roomTypes = roomType.query.all()
    return jsonify(roomTypeSchema.dump(roomTypes, many=True)), 200


@app.route('/rooms', methods=['POST'])
def createRoom():
    data = request.json
    newRoom = room(
        roomTypeID=data['roomTypeID'],
        branchId=data['branchId'],
        roomNumber=data['roomNumber'],
        price=data['price'],
        userPersonId=data['userPersonId'],
        isAvailable=True  # By default, a new room is available
    )
    db.session.add(newRoom)
    db.session.commit()
    return jsonify(roomSchema.dump(newRoom)), 201

# Route to get all rooms
@app.route('/rooms', methods=['GET'])
def getAllRooms():
    rooms = room.query.all()
    result = roomSchema.dump(rooms, many=True)
    return jsonify(result), 200

# Endpoint to fetch room availability
@app.route('/room_availability', methods=['GET'])
def get_room_availability():
    try:
        rooms = room.query.all()
        room_availability = []
        for room_obj in rooms:  # Rename the loop variable to avoid conflict
            room_data = {
                'roomNumber': room_obj.roomNumber,
                'roomTypeID': room_obj.roomTypeID,
                'isAvailable': room_obj.isAvailable
            }
            room_availability.append(room_data)
        return jsonify(room_availability)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Route to create a new booking or perform bookingTsk action
@app.route('/bookings', methods=['POST'])
def createBooking():
    try:
        data = request.json

        if 'action' in data and data['action'] == 'bookingTsk':
            # Handle bookingTsk logic here
            # Extract and process JSON data as needed
            # ...

            return jsonify({"success": True, "message": "bookingTsk processed"}), 200

        # If no 'action' specified or 'action' is not 'bookingTsk', create a new booking
        new_booking = booking(
            roomId=data['roomId'],
            customerId=data['customerId'],
            checkInDate=data['checkInDate'],
            checkOutDate=data['checkOutDate'],
            userPersonId=data['userPersonId']
        )

        db.session.add(new_booking)
        db.session.commit()

        # Assuming you have a method to generate an invoice or booking confirmation
        invoice_result = generate_invoice(new_booking)

        return jsonify({
            "success": True,
            "message": "Booking created successfully",
            "booking": bookingSchema.dump(new_booking),
            "invoice_result": invoice_result
        }), 201

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

def generate_invoice(new_booking):
    try:
        # Calculate the duration of the stay
        duration = (new_booking.checkOutDate - new_booking.checkInDate).days
        
        # Calculate the bill amount based on room price and duration of stay
        room_price = new_booking.room.price
        bill_amount = room_price * duration
        
        # Set due date to be a week after the check-out date
        due_date = new_booking.checkOutDate + timedelta(days=7)
        
        # Set the initial balance to be equal to the bill amount
        balance = bill_amount
        
        # Create a new invoice entry in the database
        new_invoice = invoice(
            customerId=new_booking.customerId,
            dueDate=due_date,
            billAmount=bill_amount,
            balance=balance,
            userPersonId=new_booking.userPersonId
        )
        
        db.session.add(new_invoice)
        db.session.commit()
        
        return invoiceSchema.dump(new_invoice)

    except Exception as e:
        print(f"Error generating invoice: {str(e)}")
        return None

# Route to create a new service type
@app.route('/serviceTypes', methods=['POST'])
def createServiceType():
    data = request.json
    newServiceType = serviceType(Name=data['name'], userPersonId=data['userPersonId'])
    db.session.add(newServiceType)
    db.session.commit()
    return jsonify(serviceTypeSchema.dump(newServiceType)), 201

# Route to create a new food
@app.route('/foods', methods=['POST'])
def createFood():
    data = request.json
    newFood = food(branchID=data['branchID'], name=data['name'],
                    price=data['price'], userPersonId=data['userPersonId'])
    db.session.add(newFood)
    db.session.commit()
    return jsonify(foodSchema.dump(newFood)), 201

# Route to create a new facility
@app.route('/facilities', methods=['POST'])
def createFacility():
    data = request.json
    newFacility = facility(branchID=data['branchID'], name=data['name'],
                            price=data['price'], userPersonId=data['userPersonId'])
    db.session.add(newFacility)
    db.session.commit()
    return jsonify(facilitySchema.dump(newFacility)), 201

# Modify the getAllInvoices route in app.py
@app.route('/invoices', methods=['GET'])
def getAllInvoices():
    invoices = invoice.query.join(customer).all()
    return jsonify(invoiceSchema.dump(invoices, many=True)), 200

@app.route('/invoices-with-names', methods=['GET'])
def get_all_invoices_with_names():
    invoices = invoice.query.join(customer).join(branch).all()
    result = []

    for inv in invoices:
        invoice_data = invoiceSchema.dump(inv)

        # Include customer and branch names in the result
        invoice_data['customerName'] = inv.customer.person.fullName
        invoice_data['branchName'] = inv.branch.name

        result.append(invoice_data)

    return jsonify(result), 200


# Route to create a new invoice or perform invoiceTsk action
@app.route('/invoices', methods=['POST'])
def create_or_update_invoice():
    try:
        data = request.json

        if 'action' in data and data['action'] == 'invoiceTsk':
            # Handle invoiceTsk logic here
            # Extract and process JSON data as needed
            # ...

            return jsonify({"success": True, "message": "invoiceTsk processed"}), 200

        # If no 'action' specified or 'action' is not 'invoiceTsk', create a new invoice
        new_invoice = invoice(
            customerId=data['customerId'],
            dueDate=data['dueDate'],
            billAmount=data['billAmount'],
            balance=data['balance'],
            userPersonId=data['userPersonId']
        )

        db.session.add(new_invoice)
        db.session.commit()

        # Assuming you have a method to generate an invoice or booking confirmation
        invoice_result = generate_invoice(new_invoice)

        return jsonify({
            "success": True,
            "message": "Invoice created successfully",
            "invoice": invoiceSchema.dump(new_invoice),
            "invoice_result": invoice_result
        }), 201

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500



# Route to get all transactions
@app.route('/transactions', methods=['GET'])
def getAllTransactions():
    transactions = transaction.query.all()
    return jsonify(transactionSchema.dump(transactions, many=True)), 200

# Route to create a new transaction

@app.route('/transactions', methods=['POST'])
def createTransaction():
    data = request.json
    newTransaction = transaction(roomId=data['roomId'], customerId=data['customerId'],
                                  serviceTypeID=data['serviceTypeID'], serviceID=data['serviceID'],
                                  quantity=data['quantity'], amount=data['amount'],
                                  invoiceID=data['invoiceID'], userPersonId=data['userPersonId'])
    db.session.add(newTransaction)
    db.session.commit()
    return jsonify(transactionSchema.dump(newTransaction)), 201

# Route to get all payments
@app.route('/payments', methods=['GET'])
def getAllPayments():
    payments = payment.query.all()
    return jsonify(paymentSchema.dump(payments, many=True)), 200

# Route to create a new payment
@app.route('/payments', methods=['POST'])
def createPayment():
    data = request.json
    newPayment = payment(amount=data['amount'], invoiceID=data['invoiceID'],
                          userPersonId=data['userPersonId'])
    db.session.add(newPayment)
    db.session.commit()
    return jsonify(paymentSchema.dump(newPayment)), 201

def create_app():
    return app

if __name__ == '__main__':
    app.run(debug=True)

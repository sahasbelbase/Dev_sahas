
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_cors import CORS

app = Flask(__name__)
app.config.from_pyfile('config.py')  

CORS(app)
ma = Marshmallow(app)
api = Api(app)

db = SQLAlchemy(app)

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
CORS(app)
ma = Marshmallow(app)
api = Api(app)

# Your existing imports
from app.models import (
    Person, User, Hotel, Branch, Customer, AddressType, Address,
    PersonAddress, HotelAddress, BranchAddress, ContactType,
    ContactInformation, RoomType, Room, Booking, ServiceType,
    Food, Facility, Invoice, Transaction, Payment
)
from app.serializers import (
    PersonSchema, UserSchema, HotelSchema, BranchSchema, CustomerSchema,
    AddressTypeSchema, AddressSchema, PersonAddressSchema, HotelAddressSchema,
    BranchAddressSchema, ContactTypeSchema, ContactInformationSchema,
    RoomTypeSchema, RoomSchema, BookingSchema, ServiceTypeSchema,
    FoodSchema, FacilitySchema, InvoiceSchema, TransactionSchema, PaymentSchema
)

# Example route to get all persons
@app.route('/persons', methods=['GET'])
def get_all_persons():
    persons = Person.query.all()
    person_schema = PersonSchema(many=True)
    result = person_schema.dump(persons)
    return jsonify(result)


# Example route to create a booking
@app.route('/api/booking', methods=['POST'])
def create_booking():
    data = request.get_json()

    # Validate Input Data
    if 'person_id' not in data or 'check_in_date' not in data:
        return jsonify(message='Invalid data. Missing required fields.'), 400

    # Create Booking
    new_booking = Booking(
        RoomId=data.get('room_id'),
        CustomerId=data.get('customer_id'),
        CheckInDate=data['check_in_date'],
        CheckOutDate=data.get('check_out_date'),
        UserPersonId=data.get('user_person_id')
    )
    db.session.add(new_booking)
    db.session.commit()

    # Check for Discount
    person_bookings = Booking.query.filter_by(
        CustomerId=data['customer_id'],
        CheckInDate=data['check_in_date']
    ).all()
    if len(person_bookings) >= 3:
        data['discount'] = 0.05

    # Serialize the booking
    booking_schema = BookingSchema()
    result = booking_schema.dump(new_booking)

    return jsonify(message='Booking created successfully', booking=result), 201


# New route for invoice
@app.route('/api/invoice')
def invoice():
    return jsonify(message='Invoice Page')  # Customize the JSON response

# New route for hotel
@app.route('/api/hotel')
def hotel():
    return jsonify(message='Hotel Page')  # Customize the JSON response

# New route for creating a customer
@app.route('/api/customer', methods=['POST'])
def create_customer():
    # Process customer form data from the request
    # You can return a success message or handle errors accordingly
    return jsonify(message='Customer created successfully')

# New route for customer
@app.route('/api/customer')
def customer():
    return jsonify(message='Customer Page')  # Customize the JSON response

# New route for creating a branch
@app.route('/api/branch', methods=['POST'])
def create_branch():
    # Process branch form data from the request
    # You can return a success message or handle errors accordingly
    return jsonify(message='Branch created successfully')

# New route for branch
@app.route('/api/branch')
def branch():
    return jsonify(message='Branch Page')  # You can customize the JSON response


if __name__ == '__main__':
    app.run(debug=True)

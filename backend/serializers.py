from marshmallow import Schema, fields
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import person, hotel, branch, customer, addressType, address, personAddress, \
    hotelAddress, branchAddress, contactType, contactInformation, personContact, hotelContact, \
    branchContact, roomType, room, booking, serviceType, food, facility, invoice, transaction, payment


class personSchema(Schema):
    class Meta:
        model = person

    personId = fields.Int(dump_only=True)
    fullName = fields.Str(required=True)
    ssn = fields.Str(required=True)
    title = fields.Str(required=True)

    
class addressTypeSchema(Schema):
    class Meta:
        model = addressType
    addressTypeId = fields.Int(dump_only=True)
    type = fields.Str(required=True)
    userPersonId = fields.Int(required=True)

class addressSchema(Schema):
    class Meta:
        model = address
    addressId = fields.Int(dump_only=True)
    addressTypeId = fields.Int(required=True)
    country = fields.Str(required=True)
    city = fields.Str(required=True)
    streetName = fields.Str(required=True)
    userPersonId = fields.Int(required=True)

class personAddressSchema(Schema):
    class Meta:
        model = personAddress
    personAddressId = fields.Int(dump_only=True)
    personId = fields.Int(required=True)
    addressId = fields.Int(required=True)
    userPersonID = fields.Int(required=True)
    insertDate = fields.DateTime()


    
class branchAddressSchema(Schema):
    class Meta:
        model = branchAddress
    branchAddressId = fields.Int(dump_only=True)
    branchId = fields.Int(required=True)
    addressId = fields.Int(required=True)
    insertDate = fields.DateTime()
    userPersonId = fields.Int(required=True)
    
class hotelAddressSchema(Schema):
    class Meta:
        model = hotelAddress

    hotelAddressId = fields.Int(dump_only=True)
    hotelId = fields.Int(required=True)
    addressId = fields.Int(required=True)
    insertDate = fields.DateTime()
    userPersonId = fields.Int(required=True)
    
    
class hotelSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = hotel
        include_relationships = True

    hotelId = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    pan = fields.Str(required=True)
    userPersonId = fields.Int(required=True)
    hotelAddress = fields.Nested(hotelAddressSchema)


class branchSchema(Schema):
    class Meta:
        model = branch
    branchId = fields.Int(dump_only=True)
    hotelId = fields.Int(required=True)
    name = fields.Str(required=True)
    userPersonId = fields.Int(required=True)

class customerSchema(Schema):
    class Meta:
        model = customer

    personId = fields.Int(required=True)
    branchId = fields.Int(required=True)
    userPersonId = fields.Int(required=True)
    insertDate = fields.DateTime()

    # Include related person information
    person = fields.Nested(personSchema)
    


class contactTypeSchema(Schema):
    class Meta:
        model = contactType
    contactTypeId = fields.Int(dump_only=True)
    type = fields.Str(required=True)
    insertDate = fields.DateTime()
    userPersonId = fields.Int(required=True)

class contactInformationSchema(Schema):
    class Meta:
        model = contactInformation
    contactInformationId = fields.Int(dump_only=True)
    contactTypeId = fields.Int(required=True)
    contact = fields.Str(required=True)
    insertDate = fields.DateTime()
    userPersonId = fields.Int(required=True)

class personContactSchema(Schema):
    class Meta:
        model = personContact
    personContactId = fields.Int(dump_only=True)
    personId = fields.Int(required=True)
    contactInformationId = fields.Int(required=True)
    insertDate = fields.DateTime()
    userPersonId = fields.Int(required=True)

class hotelContactSchema(Schema):
    class Meta:
        model = hotelContact
    hotelContactId = fields.Int(dump_only=True)
    hotelId = fields.Int(required=True)
    contactInformationId = fields.Int(required=True)
    insertDate = fields.DateTime()
    userPersonId = fields.Int(required=True)

class branchContactSchema(Schema):
    class Meta:
        model = branchContact
    branchContactId = fields.Int(dump_only=True)
    branchId = fields.Int(required=True)
    contactInformationId = fields.Int(required=True)
    insertDate = fields.DateTime()
    userPersonId = fields.Int(required=True)

class roomTypeSchema(Schema):
    class Meta:
        model = roomType
    roomTypeId = fields.Int(dump_only=True)
    roomType = fields.Str(required=True)
    insertDate = fields.DateTime()
    userPersonId = fields.Int(required=True)

class roomSchema(Schema):
    class Meta:
        model = room
    roomId = fields.Int(dump_only=True)
    roomTypeID = fields.Int(required=True)
    branchId = fields.Int(required=True)
    roomNumber = fields.Str(required=True)
    price = fields.Float(required=True)
    insertDate = fields.DateTime()
    userPersonId = fields.Int(required=True)

class bookingSchema(Schema):
    class Meta:
        model = booking
    bookingId = fields.Int(dump_only=True)
    roomId = fields.Int(required=True)
    customerId = fields.Int(required=True)
    checkInDate = fields.Date(required=True)
    checkOutDate = fields.Date(required=True)
    insertDate = fields.DateTime()
    userPersonId = fields.Int(required=True)


class serviceTypeSchema(Schema):
    class Meta:
        model = serviceType
    serviceTypeId = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    insertDate = fields.DateTime()
    userPersonId = fields.Int(required=True)

class foodSchema(Schema):
    class Meta:
        model = food
    foodId = fields.Int(dump_only=True)
    branchID = fields.Int(required=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    insertDate = fields.DateTime()
    userPersonId = fields.Int(required=True)

class facilitySchema(Schema):
    class Meta:
        model = facility
    facilityId = fields.Int(dump_only=True)
    branchID = fields.Int(required=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    insertDate = fields.DateTime()
    userPersonId = fields.Int(required=True)

class invoiceSchema(Schema):
    class Meta:
        model = invoice
    invoiceId = fields.Int(dump_only=True)
    customerId = fields.Int(required=True)
    dueDate = fields.Date(required=True)
    billAmount = fields.Float(required=True)
    balance = fields.Float(required=True)
    insertDate = fields.DateTime()
    userPersonId = fields.Int(required=True)

class transactionSchema(Schema):
    class Meta:
        model = transaction
    transactionId = fields.Int(dump_only=True)
    roomId = fields.Int(required=True)
    customerId = fields.Int(required=True)
    serviceTypeID = fields.Int(required=True)
    serviceID = fields.Int(required=True)
    quantity = fields.Str(required=True)
    amount = fields.Decimal(required=True)
    invoiceID = fields.Int()
    insertDate = fields.DateTime(dump_only=True)
    userPersonId = fields.Int(required=True)

class paymentSchema(Schema):
    class Meta:
        model = payment
    paymentId = fields.Int(dump_only=True)
    amount = fields.Float(required=True)
    invoiceID = fields.Int(required=True)
    insertDate = fields.DateTime()
    userPersonId = fields.Int(required=True)

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

class person(db.Model):
    __tablename__ = 'person'
    personId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fullName = db.Column(db.String(200), nullable=False)
    ssn = db.Column(db.String(11), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    
    
class user(db.Model):
    __tablename__ = 'user'

    userId = db.Column(db.Integer, primary_key=True)
    personId = db.Column(db.Integer, db.ForeignKey('person.personId'), nullable=False)
    branchId = db.Column(db.Integer, db.ForeignKey('branch.branchId'), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    userPersonID = db.Column(db.Integer, db.ForeignKey('person.personId'), nullable=False)
    person = db.relationship('person', foreign_keys=[personId])
    branch = db.relationship('branch', foreign_keys=[branchId])
    userPerson = db.relationship('person', foreign_keys=[userPersonID])
    
class addressType(db.Model):
    __tablename__ = 'addressType'
    addressTypeId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(200), nullable=False)
    userPersonId = db.Column(db.Integer, db.ForeignKey('person.personId'), nullable=False)
    person = db.relationship('person', foreign_keys=[userPersonId])

class address(db.Model):
    __tablename__ = 'address'
    addressId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    addressTypeId = db.Column(db.Integer, db.ForeignKey('addressType.addressTypeId'), nullable=False)
    country = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(200), nullable=False)
    streetName = db.Column(db.String(200), nullable=False)
    userPersonId = db.Column(db.Integer, db.ForeignKey('person.personId'), nullable=False)
    addressType = db.relationship('addressType', foreign_keys=[addressTypeId])
    person = db.relationship('person', foreign_keys=[userPersonId])

class hotelAddress(db.Model):
    __tablename__ = 'hotelAddress'
    hotelAddressId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hotelId = db.Column(db.Integer, db.ForeignKey('hotel.hotelId'), nullable=False)
    addressId = db.Column(db.Integer, db.ForeignKey('address.addressId'), nullable=False)
    insertDate = db.Column(db.SmallInteger, default=db.func.current_timestamp())
    userPersonId = db.Column(db.Integer, db.ForeignKey('person.personId'), nullable=False)
    hotel = db.relationship('hotel', foreign_keys=[hotelId])
    address = db.relationship('address', foreign_keys=[addressId])
    userPerson = db.relationship('person', foreign_keys=[userPersonId])
    
class hotel(db.Model):
    __tablename__ = 'hotel'
    hotelId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    pan = db.Column(db.String(10), unique=True, nullable=False)
    userPersonId = db.Column(db.Integer, db.ForeignKey('person.personId'))
    person = db.relationship('person', foreign_keys=[userPersonId])
    hotelAddress = db.relationship('hotelAddress', backref='hotel_address', uselist=False)
 
class branch(db.Model):
    __tablename__ = 'branch'
    branchId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hotelId = db.Column(db.Integer, db.ForeignKey('hotel.hotelId'), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    userPersonId = db.Column(db.Integer, db.ForeignKey('person.personId'), nullable=False)
    person = db.relationship('person', foreign_keys=[userPersonId])
    hotel = db.relationship('hotel', foreign_keys=[hotelId])
    
class customer(db.Model):
    __tablename__ = 'customer'
    personId = db.Column(db.Integer, db.ForeignKey('person.personId'), primary_key=True, nullable=False)
    branchId = db.Column(db.Integer, db.ForeignKey('branch.branchId'), nullable=False)
    userPersonId = db.Column(db.Integer, db.ForeignKey('person.personId'), nullable=False)
    insertDate = db.Column(db.SmallInteger, default=db.func.current_timestamp())    
    person = db.relationship('person', foreign_keys=[personId])
    branch = db.relationship('branch', foreign_keys=[branchId])
    userPerson = db.relationship('person', foreign_keys=[userPersonId])

class personAddress(db.Model):
    __tablename__ = 'personAddress'
    personAddressId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    personId = db.Column(db.Integer, db.ForeignKey('person.personId'), nullable=False)
    addressId = db.Column(db.Integer, db.ForeignKey('address.addressId'), nullable=False)  # Add ForeignKey here
    userPersonID = db.Column(db.Integer, db.ForeignKey('person.personId'), nullable=False)
    insertDate = db.Column(db.SmallInteger, default=db.func.current_timestamp())
    person = db.relationship('person', foreign_keys=[personId])
    address = db.relationship('address', foreign_keys=[addressId])
    userPerson = db.relationship('person', foreign_keys=[userPersonID])

class branchAddress(db.Model):
    __tablename__ = 'branchAddress'
    branchAddressId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    branchId = db.Column(db.Integer, db.ForeignKey('branch.branchId'), nullable=False)
    addressId = db.Column(db.Integer, db.ForeignKey('address.addressId'), nullable=False)
    insertDate = db.Column(db.SmallInteger, default=db.func.current_timestamp())
    userPersonId = db.Column(db.Integer, db.ForeignKey('person.personId'), nullable=False)
    branch = db.relationship('branch', foreign_keys=[branchId])
    address = db.relationship('address', foreign_keys=[addressId])
    userPerson = db.relationship('person', foreign_keys=[userPersonId])    
    
class contactType(db.Model):
    __tablename__ = 'contactType'
    contactTypeId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(200), nullable=False)
    insertDate = db.Column(db.SmallInteger, default=db.func.current_timestamp())
    userPersonId = db.Column(db.Integer, db.ForeignKey('person.personId'), nullable=False)
    person = db.relationship('person', foreign_keys=[userPersonId])
class contactInformation(db.Model):
    __tablename__ = 'contactInformation'
    contactInformationId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    contactTypeId = db.Column(db.Integer, db.ForeignKey('contactType.contactTypeId'), nullable=False)
    contact = db.Column(db.String(200), nullable=False)
    insertDate = db.Column(db.SmallInteger, default=db.func.current_timestamp())
    userPersonId = db.Column(db.Integer, db.ForeignKey('person.personId'), nullable=False)
    contactType = db.relationship('contactType', foreign_keys=[contactTypeId])
    person = db.relationship('person', foreign_keys=[userPersonId])
class personContact(db.Model):
    __tablename__ = 'personContact'
    personContactId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    personId = db.Column(db.Integer, db.ForeignKey('person.personId'), nullable=False)
    contactInformationId = db.Column(db.Integer, db.ForeignKey('contactInformation.contactInformationId'), nullable=False)
    insertDate = db.Column(db.SmallInteger, default=db.func.current_timestamp())
    userPersonId = db.Column(db.Integer, db.ForeignKey('person.personId'), nullable=False)
    person = db.relationship('person', foreign_keys=[personId])
    contactInfo = db.relationship('contactInformation', foreign_keys=[contactInformationId])
    userPerson = db.relationship('person', foreign_keys=[userPersonId])
class hotelContact(db.Model):
    __tablename__ = 'hotelContact'
    hotelContactId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hotelId = db.Column(db.Integer, db.ForeignKey('hotel.hotelId'), nullable=False)
    contactInformationId = db.Column(db.Integer, db.ForeignKey('contactInformation.contactInformationId'), nullable=False)
    insertDate = db.Column(db.SmallInteger, default=db.func.current_timestamp())
    userPersonId = db.Column(db.Integer, db.ForeignKey('person.personId'), nullable=False)
    hotel = db.relationship('hotel', foreign_keys=[hotelId])
    contactInfo = db.relationship('contactInformation', foreign_keys=[contactInformationId])
    userPerson = db.relationship('person', foreign_keys=[userPersonId])
class branchContact(db.Model):
    __tablename__ = 'branchContact'
    branchContactId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    branchId = db.Column(db.Integer, db.ForeignKey('branch.branchId'), nullable=False)
    contactInformationId = db.Column(db.Integer, db.ForeignKey('contactInformation.contactInformationId'), nullable=False)
    insertDate = db.Column(db.SmallInteger, default=db.func.current_timestamp())
    userPersonId = db.Column(db.Integer, db.ForeignKey('person.personId'), nullable=False)
    branch = db.relationship('branch', foreign_keys=[branchId])
    contactInfo = db.relationship('contactInformation', foreign_keys=[contactInformationId])
    userPerson = db.relationship('person', foreign_keys=[userPersonId])
class roomType(db.Model):
    __tablename__ = 'roomType'
    roomTypeId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    roomType = db.Column(db.String(200), nullable=False)
    insertDate = db.Column(db.SmallInteger, default=db.func.current_timestamp())
    userPersonId = db.Column(db.Integer, db.ForeignKey('person.personId'), nullable=True)
    person = db.relationship('person', foreign_keys=[userPersonId])
class room(db.Model):
    __tablename__ = 'room'
    roomId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    roomTypeID = db.Column(db.Integer, db.ForeignKey('roomType.roomTypeId'), nullable=False)
    branchId = db.Column(db.Integer, db.ForeignKey('branch.branchId'), nullable=False)
    roomNumber = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    insertDate = db.Column(db.SmallInteger, default=db.func.current_timestamp())
    userPersonId = db.Column(db.Integer, db.ForeignKey('person.personId'), nullable=True)
    isAvailable = db.Column(db.String(10), nullable=False, default='Available')  # Updated field for availability
    roomType = db.relationship('roomType', foreign_keys=[roomTypeID])
    branch = db.relationship('branch', foreign_keys=[branchId])
    userPerson = db.relationship('person', foreign_keys=[userPersonId])

class booking(db.Model):
    __tablename__ = 'booking'
    bookingId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    roomId = db.Column(db.Integer, db.ForeignKey('room.roomId'), nullable=False)
    customerId = db.Column(db.Integer, db.ForeignKey('customer.personId'), nullable=True)
    checkInDate = db.Column(db.Date, nullable=False)
    checkOutDate = db.Column(db.Date, nullable=False)
    insertDate = db.Column(db.SmallInteger, default=db.func.current_timestamp())
    userPersonId = db.Column(db.Integer, db.ForeignKey('person.personId'), nullable=True)
    room = db.relationship('room', foreign_keys=[roomId])
    customer = db.relationship('customer', foreign_keys=[customerId])
    userPerson = db.relationship('person', foreign_keys=[userPersonId])
class serviceType(db.Model):
    __tablename__ = 'serviceType'
    serviceTypeId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    insertDate = db.Column(db.SmallInteger, default=db.func.current_timestamp())
    userPersonId = db.Column(db.Integer, db.ForeignKey('person.personId'), nullable=False)
    person = db.relationship('person', foreign_keys=[userPersonId])
class food(db.Model):
    __tablename__ = 'food'
    foodId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    branchID = db.Column(db.Integer, db.ForeignKey('branch.branchId'), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    insertDate = db.Column(db.SmallInteger, default=db.func.current_timestamp())
    userPersonId = db.Column(db.Integer, db.ForeignKey('person.personId'), nullable=False)
    branch = db.relationship('branch', foreign_keys=[branchID])
    userPerson = db.relationship('person', foreign_keys=[userPersonId])

class facility(db.Model):
    __tablename__ = 'facility'
    facilityId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    branchID = db.Column(db.Integer, db.ForeignKey('branch.branchId'), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    insertDate = db.Column(db.SmallInteger, default=db.func.current_timestamp())
    userPersonId = db.Column(db.Integer, db.ForeignKey('person.personId'), nullable=False)
    branch = db.relationship('branch', foreign_keys=[branchID])
    userPerson = db.relationship('person', foreign_keys=[userPersonId])
class invoice(db.Model):
    __tablename__ = 'invoice'
    invoiceId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customerId = db.Column(db.Integer, db.ForeignKey('customer.personId'), nullable=False)
    dueDate = db.Column(db.SmallInteger, nullable=False)
    billAmount = db.Column(db.Float, nullable=False)
    balance = db.Column(db.Float, nullable=False)
    insertDate = db.Column(db.SmallInteger, default=db.func.current_timestamp())
    userPersonId = db.Column(db.Integer, db.ForeignKey('person.personId'), nullable=False)
    customer = db.relationship('customer', foreign_keys=[customerId])
    userPerson = db.relationship('person', foreign_keys=[userPersonId])
 
class transaction(db.Model):
    transactionId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    roomId = db.Column(db.Integer, db.ForeignKey('room.roomId'), nullable=False)
    customerId = db.Column(db.Integer, db.ForeignKey('customer.personId'), nullable=False)
    serviceTypeID = db.Column(db.Integer, db.ForeignKey('serviceType.serviceTypeId'), nullable=False)
    serviceID = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.DECIMAL(10, 2), nullable=False)
    invoiceID = db.Column(db.Integer, db.ForeignKey('invoice.invoiceId'))
    insertDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    userPersonId = db.Column(db.Integer, db.ForeignKey('person.personId'), nullable=False)  # Add ForeignKey here
    room = db.relationship('room', foreign_keys=[roomId])
    customer = db.relationship('customer', foreign_keys=[customerId])
    user = db.relationship('person', foreign_keys=[userPersonId])
    serviceType = db.relationship('serviceType', foreign_keys=[serviceTypeID])
    invoice = db.relationship('invoice', foreign_keys=[invoiceID])


class payment(db.Model):
    __tablename__ = 'payment'
    paymentId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Float, nullable=False)
    invoiceID = db.Column(db.Integer, db.ForeignKey('invoice.invoiceId'), nullable=False)
    insertDate = db.Column(db.SmallInteger, default=db.func.current_timestamp())
    userPersonId = db.Column(db.Integer, db.ForeignKey('person.personId'), nullable=False)
    invoice = db.relationship('invoice', foreign_keys=[invoiceID])
    userPerson = db.relationship('person', foreign_keys=[userPersonId])


def init_app(app):
    db.init_app(app)
    

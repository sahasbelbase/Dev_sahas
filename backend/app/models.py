from app import db 

class Person(db.Model):
    PersonId = db.Column(db.Integer, primary_key=True)
    FullName = db.Column(db.String(200), nullable=False)
    SSN = db.Column(db.String(11), nullable=False)
    Title = db.Column(db.String(200), nullable=False)
    InsertDate = db.Column(db.DateTime, default=db.func.current_timestamp())

class User(db.Model):
    PersonId = db.Column(db.Integer, primary_key=True, nullable=False)
    BranchId = db.Column(db.Integer, nullable=False)
    Username = db.Column(db.String(200), nullable=False)
    Password = db.Column(db.String(200), nullable=False)
    InsertDate = db.Column(db.DateTime, default=db.func.current_timestamp())
    UserPersonID = db.Column(db.Integer, db.ForeignKey('person.PersonId'))

class Hotel(db.Model):
    HotelId = db.Column(db.Integer, primary_key=True, nullable=False)
    Name = db.Column(db.String(200), nullable=False)
    PAN = db.Column(db.String(10), unique=True, nullable=False)
    UserPersonId = db.Column(db.Integer, db.ForeignKey('person.PersonId'), nullable=False)
    InsertDate = db.Column(db.DateTime, default=db.func.current_timestamp())

class Branch(db.Model):
    BranchId = db.Column(db.Integer, primary_key=True, nullable=False)
    HotelId = db.Column(db.Integer, nullable=False)
    Name = db.Column(db.String(200), nullable=False)
    UserPersonId = db.Column(db.Integer, db.ForeignKey('person.PersonId'), nullable=False)
    InsertDate = db.Column(db.DateTime, default=db.func.current_timestamp())

class Customer(db.Model):
    PersonId = db.Column(db.Integer, primary_key=True, nullable=False)
    BranchId = db.Column(db.Integer, nullable=False)
    UserPersonId = db.Column(db.Integer, nullable=False)
    InsertDate = db.Column(db.DateTime, default=db.func.current_timestamp())

class AddressType(db.Model):
    AddressTypeId = db.Column(db.Integer, primary_key=True, nullable=False)
    Type = db.Column(db.String(200), nullable=False)
    UserPersonId = db.Column(db.Integer, db.ForeignKey('user.PersonId'), nullable=False)
    InsertDate = db.Column(db.DateTime, default=db.func.current_timestamp())

class Address(db.Model):
    AddressId = db.Column(db.Integer, primary_key=True, nullable=False)
    AddressTypeId = db.Column(db.Integer, nullable=False)
    Country = db.Column(db.String(200), nullable=False)
    City = db.Column(db.String(200), nullable=False)
    StreetName = db.Column(db.String(200), nullable=False)
    InsertDate = db.Column(db.DateTime, default=db.func.current_timestamp())
    UserPersonId = db.Column(db.Integer, db.ForeignKey('user.PersonId'), nullable=False)

class PersonAddress(db.Model):
    PersonAddressId = db.Column(db.Integer, primary_key=True, nullable=False)
    PersonId = db.Column(db.Integer, nullable=False)
    AddressId = db.Column(db.Integer, nullable=False)
    UserPersonID = db.Column(db.Integer, nullable=False)
    InsertDate = db.Column(db.DateTime, default=db.func.current_timestamp())

class HotelAddress(db.Model):
    HotelAddressId = db.Column(db.Integer, primary_key=True, nullable=False)
    HotelId = db.Column(db.Integer, nullable=False)
    AddressId = db.Column(db.Integer, nullable=False)
    InsertDate = db.Column(db.DateTime, default=db.func.current_timestamp())
    UserPersonId = db.Column(db.Integer, db.ForeignKey('user.PersonId'))

class BranchAddress(db.Model):
    BranchAddressId = db.Column(db.Integer, primary_key=True, nullable=False)
    BranchId = db.Column(db.Integer, nullable=False)
    AddressId = db.Column(db.Integer, nullable=False)
    InsertDate = db.Column(db.DateTime, default=db.func.current_timestamp())
    UserPersonId = db.Column(db.Integer, nullable=False)

class ContactType(db.Model):
    ContactTypeId = db.Column(db.Integer, primary_key=True, nullable=False)
    Type = db.Column(db.String(200), nullable=False)
    InsertDate = db.Column(db.DateTime, default=db.func.current_timestamp())
    UserPersonId = db.Column(db.Integer, nullable=False)

class ContactInformation(db.Model):
    ContactInformationId = db.Column(db.Integer, primary_key=True, nullable=False)
    ContactTypeId = db.Column(db.Integer, nullable=False)
    Contact = db.Column(db.String(200), nullable=False)
    InsertDate = db.Column(db.DateTime, default=db.func.current_timestamp())
    UserPersonId = db.Column(db.Integer, nullable=False)

class RoomType(db.Model):
    RoomTypeId = db.Column(db.Integer, primary_key=True, nullable=False)
    RoomType = db.Column(db.String(200), nullable=False)
    InsertDate = db.Column(db.DateTime, default=db.func.current_timestamp())
    UserPersonId = db.Column(db.Integer, nullable=False)

class Room(db.Model):
    RoomId = db.Column(db.Integer, primary_key=True, nullable=False)
    RoomTypeID = db.Column(db.Integer, nullable=False)
    BranchId = db.Column(db.Integer, nullable=False)
    RoomNumber = db.Column(db.String(50), nullable=False)
    Price = db.Column(db.Float, nullable=False)
    InsertDate = db.Column(db.DateTime, default=db.func.current_timestamp())
    UserPersonId = db.Column(db.Integer, db.ForeignKey('user.PersonId'), nullable=False)

class Booking(db.Model):
    BookingId = db.Column(db.Integer, primary_key=True, nullable=False)
    RoomId = db.Column(db.Integer, nullable=False)
    CustomerId = db.Column(db.Integer, nullable=False)
    CheckInDate = db.Column(db.Date, nullable=False)
    CheckOutDate = db.Column(db.Date, nullable=False)
    InsertDate = db.Column(db.DateTime, default=db.func.current_timestamp())
    UserPersonId = db.Column(db.Integer, db.ForeignKey('user.PersonId'), nullable=False)

class ServiceType(db.Model):
    ServiceTypeId = db.Column(db.Integer, primary_key=True, nullable=False)
    Name = db.Column(db.String(200), nullable=False)
    InsertDate = db.Column(db.DateTime, default=db.func.current_timestamp())
    UserPersonId = db.Column(db.Integer, db.ForeignKey('user.PersonId'), nullable=False)

class Food(db.Model):
    FoodId = db.Column(db.Integer, primary_key=True, nullable=False)
    BranchID = db.Column(db.Integer, nullable=False)
    Name = db.Column(db.String(200), nullable=False)
    Price = db.Column(db.Float, nullable=False)
    InsertDate = db.Column(db.DateTime, default=db.func.current_timestamp())
    UserPersonId = db.Column(db.Integer, db.ForeignKey('user.PersonId'), nullable=False)

class Facility(db.Model):
    FacilityId = db.Column(db.Integer, primary_key=True, nullable=False)
    BranchID = db.Column(db.Integer, nullable=False)
    Name = db.Column(db.String(200), nullable=False)
    Price = db.Column(db.Float, nullable=False)
    InsertDate = db.Column(db.DateTime, default=db.func.current_timestamp())
    UserPersonId = db.Column(db.Integer, db.ForeignKey('user.PersonId'), nullable=False)

class Invoice(db.Model):
    InvoiceId = db.Column(db.Integer, primary_key=True, nullable=False)
    CustomerId = db.Column(db.Integer, nullable=False)
    DueDate = db.Column(db.Date, nullable=False)
    BillAmount = db.Column(db.Float, nullable=False)
    Balance = db.Column(db.Float, nullable=False)
    InsertDate = db.Column(db.DateTime, default=db.func.current_timestamp())
    UserPersonId = db.Column(db.Integer, db.ForeignKey('user.PersonId'), nullable=False)

class Transaction(db.Model):
    TransactionId = db.Column(db.Integer, primary_key=True, nullable=False)
    RoomId = db.Column(db.Integer, nullable=False)
    CustomerId = db.Column(db.Integer, nullable=False)
    ServiceTypeID = db.Column(db.Integer, nullable=False)
    ServiceID = db.Column(db.Integer, nullable=False)
    Quantity = db.Column(db.String(100), nullable=False)
    Amount = db.Column(db.Float, nullable=False)
    InvoiceID = db.Column(db.Integer, nullable=True)
    InsertDate = db.Column(db.DateTime, default=db.func.current_timestamp())
    UserPersonId = db.Column(db.Integer, db.ForeignKey('user.PersonId'), nullable=False)

class Payment(db.Model):
    PaymentId = db.Column(db.Integer, primary_key=True, nullable=False)
    Amount = db.Column(db.Float, nullable=False)
    InvoiceID = db.Column(db.Integer, nullable=False)
    InsertDate = db.Column(db.DateTime, default=db.func.current_timestamp())
    UserPersonId = db.Column(db.Integer, db.ForeignKey('user.PersonId'), nullable=False)

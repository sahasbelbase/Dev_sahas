from app import ma
from app.models import Person, User, Hotel, Branch, Customer, AddressType, Address, PersonAddress, HotelAddress, \
    BranchAddress, ContactType, ContactInformation, RoomType, Room, Booking, ServiceType, Food, Facility, Invoice, \
    Transaction, Payment
    
class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person        
        
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

class HotelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Hotel

class BranchSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Branch

class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer

class AddressTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AddressType

class AddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Address

class PersonAddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PersonAddress

class HotelAddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = HotelAddress

class BranchAddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BranchAddress

class ContactTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ContactType

class ContactInformationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ContactInformation

class RoomTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RoomType

class RoomSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Room

class BookingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Booking

class ServiceTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ServiceType

class FoodSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Food

class FacilitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Facility

class InvoiceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Invoice

class TransactionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Transaction

class PaymentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Payment
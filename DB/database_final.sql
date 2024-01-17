-- Create the HotelReserveSys database
CREATE DATABASE HotelReserveSys;

-- Define the Person table
CREATE TABLE Person (
    PersonId INT IDENTITY(1,1) PRIMARY KEY, -- Unique identifier for a person
    FullName VARCHAR(200) NOT NULL, -- Full name of the person
    SSN VARCHAR(11) NOT NULL, -- Social Security Number of the person
    Title VARCHAR(200) NOT NULL, -- Title of the person (e.g., Mr., Mrs., Dr.)
    InsertDate SMALLDATETIME DEFAULT(GETDATE()) -- Date when the record is inserted
);

-- Adding an index on SSN for faster lookups
CREATE INDEX IX_Person_SSN ON Person(SSN);

-- Define the User table
CREATE TABLE [User] (
    PersonId INT PRIMARY KEY NOT NULL, -- Unique identifier for a user
    BranchId INT NOT NULL, -- Identifier for the branch associated with the user
    Username VARCHAR(200) NOT NULL, -- Username for login
    Password VARCHAR(200) NOT NULL, -- Password for login
    InsertDate SMALLDATETIME DEFAULT(GETDATE()), -- Date when the record is inserted
    UserPersonID INT, -- Identifier linking to the Person table
    CONSTRAINT FkUserPersonID FOREIGN KEY (PersonId) REFERENCES Person (PersonId),
    CONSTRAINT FkUserUserPersonID FOREIGN KEY (UserPersonId) REFERENCES Person (PersonId),
    CONSTRAINT FkUserBranchID FOREIGN KEY (BranchId) REFERENCES Branch (BranchId)
);

-- Adding an index on Username for faster lookups
CREATE INDEX IX_User_Username ON [User](Username);

-- Define the Hotel table
CREATE TABLE Hotel (
    HotelId INT IDENTITY(1,1) PRIMARY KEY NOT NULL, -- Unique identifier for a hotel
    [Name] VARCHAR(200) NOT NULL, -- Name of the hotel
    PAN VARCHAR(10) UNIQUE NOT NULL, -- Permanent Account Number of the hotel
    UserPersonId INT, -- Identifier linking to the Person table
    InsertDate SMALLDATETIME DEFAULT(GETDATE()), -- Date when the record is inserted
    CONSTRAINT FkHotelPersonID FOREIGN KEY (UserPersonId) REFERENCES Person (PersonId)
);

-- Adding an index on PAN for faster lookups
CREATE INDEX IX_Hotel_PAN ON Hotel(PAN);

-- Define the Branch table
CREATE TABLE Branch (
    BranchId INT IDENTITY(1,1) PRIMARY KEY NOT NULL, -- Unique identifier for a branch
    HotelId INT NOT NULL, -- Identifier for the hotel associated with the branch
    [Name] VARCHAR(200) NOT NULL, -- Name of the branch
    UserPersonId INT, -- Identifier linking to the Person table
    InsertDate SMALLDATETIME DEFAULT(GETDATE()), -- Date when the record is inserted
    CONSTRAINT FkBranchPersonID FOREIGN KEY (UserPersonId) REFERENCES Person (PersonId),
    CONSTRAINT FkBranchHotelID FOREIGN KEY (HotelId) REFERENCES Hotel (HotelId)
);

-- Adding an index on Branch Name for faster lookups
CREATE INDEX IX_Branch_Name ON Branch([Name]);

-- Define the Customer table
CREATE TABLE Customer (
    PersonId INT PRIMARY KEY NOT NULL, -- Unique identifier for a customer
    BranchId INT NOT NULL, -- Identifier for the branch associated with the customer
    UserPersonId INT NOT NULL, -- Identifier linking to the [User] table
    InsertDate SMALLDATETIME DEFAULT(GETDATE()), -- Date when the record is inserted
    CONSTRAINT FkCustomerPersonID FOREIGN KEY (PersonId) REFERENCES Person (PersonId),
    CONSTRAINT FkCustomerUserPersonID FOREIGN KEY (UserPersonId) REFERENCES [User] (PersonId),
    CONSTRAINT FkCustomerBranchID FOREIGN KEY (BranchId) REFERENCES Branch (BranchId)
);

-- Adding an index on Customer PersonId for faster lookups
CREATE INDEX IX_Customer_PersonId ON Customer(PersonId);

-- Define the AddressType table
CREATE TABLE [AddressType] (
    AddressTypeId INT IDENTITY(1,1) PRIMARY KEY NOT NULL, -- Unique identifier for an address type
    [Type] VARCHAR(200) NOT NULL, -- Type of address (e.g., Home, Office)
    UserPersonId INT NOT NULL, -- Identifier linking to the [User] table
    InsertDate SMALLDATETIME DEFAULT(GETDATE()), -- Date when the record is inserted
    CONSTRAINT FkAddressTypeUserPersonID FOREIGN KEY (UserPersonId) REFERENCES [User] (PersonId)
);

-- Define the Address table
CREATE TABLE [Address] (
    AddressId INT IDENTITY(1,1) PRIMARY KEY, -- Unique identifier for an address
    AddressTypeId INT NOT NULL, -- Identifier for the address type
    Country VARCHAR(200) NOT NULL, -- Country of the address
    City VARCHAR(200) NOT NULL, -- City of the address
    StreetName VARCHAR(200) NOT NULL, -- Street name of the address
    InsertDate SMALLDATETIME DEFAULT(GETDATE()), -- Date when the record is inserted
    UserPersonId INT NOT NULL, -- Identifier linking to the [User] table
    CONSTRAINT FkAddressAddressTypeID FOREIGN KEY (AddressTypeId) REFERENCES [AddressType] (AddressTypeId),
    CONSTRAINT FkAddressUserPersonID FOREIGN KEY (UserPersonId) REFERENCES [User] (PersonId)
);

-- Adding an index on Country for faster lookups
CREATE INDEX IX_Address_Country ON [Address](Country);

-- Define the PersonAddress table
CREATE TABLE [PersonAddress] (
    PersonAddressId INT IDENTITY(1,1) PRIMARY KEY, -- Unique identifier for a person address
    PersonId INT NOT NULL, -- Identifier for the person associated with the address
    AddressId INT NOT NULL, -- Identifier for the address associated with the person
    UserPersonID INT NOT NULL, -- Identifier linking to the [User] table
    InsertDate SMALLDATETIME DEFAULT(GETDATE()), -- Date when the record is inserted
    CONSTRAINT FkPersonAddressPersonID FOREIGN KEY (PersonId) REFERENCES Person (PersonId),
    CONSTRAINT FkPersonAddressID FOREIGN KEY (AddressId) REFERENCES [Address] (AddressId),
    CONSTRAINT FkPersonAddressUserPersonID FOREIGN KEY (UserPersonId) REFERENCES [User] (PersonId)
);

-- Define the HotelAddress table
CREATE TABLE [HotelAddress] (
    HotelAddressId INT IDENTITY(1,1) PRIMARY KEY, -- Unique identifier for a hotel address
    HotelId INT NOT NULL, -- Identifier for the hotel associated with the address
    AddressId INT NOT NULL, -- Identifier for the address associated with the hotel
    InsertDate SMALLDATETIME NOT NULL DEFAULT(GETDATE()), -- Date when the record is inserted
    UserPersonId INT, -- Identifier linking to the [User] table
    CONSTRAINT FkHotelAddressHotelID FOREIGN KEY(HotelId) REFERENCES Hotel(HotelId),
    CONSTRAINT FkHotelAddressAddressID FOREIGN KEY(AddressId) REFERENCES [Address](AddressId),
    CONSTRAINT FkHotelAddressUserPersonID FOREIGN KEY (UserPersonId) REFERENCES [User] (PersonId)
);

-- Define the BranchAddress table
CREATE TABLE [BranchAddress] (
    BranchAddressId INT IDENTITY(1,1) PRIMARY KEY, -- Unique identifier for a branch address
    BranchId INT NOT NULL, -- Identifier for the branch associated with the address
    AddressId INT NOT NULL, -- Identifier for the address associated with the branch
    InsertDate SMALLDATETIME NOT NULL DEFAULT(GETDATE()), -- Date when the record is inserted
    UserPersonId INT NOT NULL, -- Identifier linking to the [User] table
    CONSTRAINT FkBranchAddressBranchID FOREIGN KEY(BranchId) REFERENCES Branch(BranchId),
    CONSTRAINT FkBranchAddressAddressID FOREIGN KEY(AddressId) REFERENCES [Address](AddressId),
    CONSTRAINT FkBranchAddressUserPersonID FOREIGN KEY (UserPersonId) REFERENCES [User] (PersonId)
);

-- Define the ContactType table
CREATE TABLE [ContactType] (
    ContactTypeId INT IDENTITY(1,1) PRIMARY KEY, -- Unique identifier for a contact type
    [Type] VARCHAR(200) NOT NULL, -- Type of contact (e.g., Email, Phone)
    InsertDate SMALLDATETIME NOT NULL DEFAULT(GETDATE()), -- Date when the record is inserted
    UserPersonId INT NOT NULL, -- Identifier linking to the [User] table
    CONSTRAINT FkContactTypeUserPersonID FOREIGN KEY (UserPersonId) REFERENCES [User] (PersonId)
);

-- Define the ContactInformation table
CREATE TABLE [ContactInformation] (
    ContactInformationId INT IDENTITY(1,1) PRIMARY KEY, -- Unique identifier for contact information
    ContactTypeId INT NOT NULL, -- Identifier for the contact type
    Contact VARCHAR(200) NOT NULL, -- Actual contact information (e.g., email address, phone number)
    InsertDate SMALLDATETIME NOT NULL DEFAULT(GETDATE()), -- Date when the record is inserted
    UserPersonId INT NOT NULL, -- Identifier linking to the [User] table
    CONSTRAINT FkContactInformationContactTypeID FOREIGN KEY(ContactTypeId) REFERENCES [ContactType](ContactTypeId),
    CONSTRAINT FkContactInformationUserPersonID FOREIGN KEY (UserPersonId) REFERENCES [User] (PersonId)
);

-- Define the PersonContact table
CREATE TABLE [PersonContact] (
    PersonContactId INT IDENTITY(1,1) PRIMARY KEY, -- Unique identifier for a person's contact
    PersonId INT NOT NULL, -- Identifier for the person associated with the contact
    ContactInformationId INT NOT NULL, -- Identifier for the contact information associated with the person
    InsertDate SMALLDATETIME NOT NULL DEFAULT(GETDATE()), -- Date when the record is inserted
    UserPersonId INT NOT NULL, -- Identifier linking to the [User] table
    CONSTRAINT FkPersonContactPersonID FOREIGN KEY(PersonId) REFERENCES Person(PersonId),
    CONSTRAINT FkPersonContactContactInformationID FOREIGN KEY(ContactInformationId) REFERENCES [ContactInformation](ContactInformationId),
    CONSTRAINT FkPersonContactUserPersonID FOREIGN KEY (UserPersonId) REFERENCES [User] (PersonId)
);

-- Define the HotelContact table
CREATE TABLE [HotelContact] (
    HotelContactId INT IDENTITY(1,1) PRIMARY KEY, -- Unique identifier for a hotel contact
    HotelId INT NOT NULL, -- Identifier for the hotel associated with the contact
    ContactInformationId INT NOT NULL, -- Identifier for the contact information associated with the hotel
    InsertDate SMALLDATETIME NOT NULL DEFAULT(GETDATE()), -- Date when the record is inserted
    UserPersonId INT NOT NULL, -- Identifier linking to the [User] table
    CONSTRAINT FkHotelContactHotelID FOREIGN KEY(HotelId) REFERENCES Hotel(HotelId),
    CONSTRAINT FkHotelContactContactInformationID FOREIGN KEY(ContactInformationId) REFERENCES [ContactInformation](ContactInformationId),    
    CONSTRAINT FkHotelContactUserPersonID FOREIGN KEY (UserPersonId) REFERENCES [User] (PersonId)
);

-- Define the BranchContact table
CREATE TABLE [BranchContact] (
    BranchContactId INT IDENTITY(1,1) PRIMARY KEY, -- Unique identifier for a branch contact
    BranchId INT NOT NULL, -- Identifier for the branch associated with the contact
    ContactInformationId INT NOT NULL, -- Identifier for the contact information associated with the branch
    InsertDate SMALLDATETIME NOT NULL DEFAULT(GETDATE()), -- Date when the record is inserted
    UserPersonId INT NOT NULL, -- Identifier linking to the [User] table
    CONSTRAINT FkBranchContactBranchID FOREIGN KEY(BranchID) REFERENCES Branch(BranchId),
    CONSTRAINT FkBranchContactContactInformationID FOREIGN KEY(ContactInformationId) REFERENCES [ContactInformation](ContactInformationId),
    CONSTRAINT FkBranchContactUserPersonID FOREIGN KEY (UserPersonId) REFERENCES [User] (PersonId)
);

-- Define the RoomType table
CREATE TABLE [RoomType] (
    RoomTypeId INT IDENTITY(1,1) PRIMARY KEY, -- Unique identifier for a room type
    RoomType VARCHAR(200) NOT NULL, -- Type of room (e.g., Single, Double)
    InsertDate SMALLDATETIME NOT NULL DEFAULT(GETDATE()), -- Date when the record is inserted
    UserPersonId INT NOT NULL, -- Identifier linking to the [User] table
    CONSTRAINT FkRoomTypeUserPersonID FOREIGN KEY (UserPersonId) REFERENCES [User] (PersonId)
);

-- Define the Room table
CREATE TABLE [Room] (
    RoomId INT IDENTITY(1,1) PRIMARY KEY, -- Unique identifier for a room
    RoomTypeID INT NOT NULL, -- Identifier for the room type
    BranchId INT NOT NULL, -- Identifier for the branch associated with the room
    RoomNumber VARCHAR(50) NOT NULL, -- Room number
    Price MONEY NOT NULL, -- Price for the room
    InsertDate SMALLDATETIME NOT NULL DEFAULT(GETDATE()), -- Date when the record is inserted
    UserPersonId INT NOT NULL, -- Identifier linking to the [User] table
    CONSTRAINT FkRoomUserPersonID FOREIGN KEY (UserPersonId) REFERENCES [User] (PersonId),
    CONSTRAINT FkRoomRoomTypeID FOREIGN KEY (RoomTypeID) REFERENCES [RoomType] (RoomTypeID)
);


-- Creating the Booking table to store information about room bookings
CREATE TABLE [Booking](
    BookingId INT IDENTITY(1,1) PRIMARY KEY, -- Unique identifier for each booking
    RoomId INT NOT NULL, -- Reference to the booked room
    CustomerId INT NOT NULL, -- Reference to the customer making the booking
    CheckInDate DATE NOT NULL, -- Date when the customer checks in
    CheckOutDate DATE NOT NULL, -- Date when the customer checks out
    InsertDate SMALLDATETIME NOT NULL CONSTRAINT DfBookingInsertDate DEFAULT(GETDATE()), -- Date when the booking record is inserted
    UserPersonId INT NOT NULL, -- Reference to the user responsible for the booking
    CONSTRAINT FkBookingRoomID FOREIGN KEY (RoomID) REFERENCES [Room] (RoomID), -- Foreign key relationship with the Room table
    CONSTRAINT FkBookingCustomerID FOREIGN KEY (CustomerID) REFERENCES [Customer] (PersonID), -- Foreign key relationship with the Customer table
    CONSTRAINT FkBookingUserPersonID FOREIGN KEY (UserPersonId) REFERENCES [User] (PersonId) -- Foreign key relationship with the User table
);

-- Creating the ServiceType table to store types of services offered
CREATE TABLE [ServiceType](
    ServiceTypeId INT IDENTITY(1,1) PRIMARY KEY, -- Unique identifier for each service type
    [Name] VARCHAR(200) NOT NULL, -- Name of the service type
    InsertDate SMALLDATETIME NOT NULL CONSTRAINT DfServiceTypeInsertDate DEFAULT(GETDATE()), -- Date when the service type record is inserted
    UserPersonId INT NOT NULL, -- Reference to the user responsible for adding the service type
    CONSTRAINT FkServiceTypeUserPersonID FOREIGN KEY (UserPersonId) REFERENCES [User] (PersonId) -- Foreign key relationship with the User table
);

-- Creating the Food table to store information about food items
CREATE TABLE [Food](
    FoodId INT IDENTITY(1,1) PRIMARY KEY, -- Unique identifier for each food item
    BranchID INT NOT NULL, -- Reference to the branch offering the food item
    Name VARCHAR(200) NOT NULL, -- Name of the food item
    Price MONEY NOT NULL, -- Price of the food item
    InsertDate SMALLDATETIME NOT NULL CONSTRAINT DfFoodInsertDate DEFAULT(GETDATE()), -- Date when the food item record is inserted
    UserPersonId INT NOT NULL, -- Reference to the user responsible for adding the food item
    CONSTRAINT FkFoodServiceTypeID FOREIGN KEY (BranchId) REFERENCES [Branch] (branchId), -- Foreign key relationship with the Branch table
    CONSTRAINT FkFoodUserPersonID FOREIGN KEY (UserPersonId) REFERENCES [User] (PersonId) -- Foreign key relationship with the User table
);

-- Creating the Facility table to store information about facilities offered
CREATE TABLE [Facility](
    FacilityId INT IDENTITY(1,1) PRIMARY KEY, -- Unique identifier for each facility
    BranchID INT NOT NULL, -- Reference to the branch offering the facility
    [Name] VARCHAR(200) NOT NULL, -- Name of the facility
    Price MONEY NOT NULL, -- Price of the facility
    InsertDate SMALLDATETIME NOT NULL CONSTRAINT DfFacilityInsertDate DEFAULT(GETDATE()), -- Date when the facility record is inserted
    UserPersonId INT NOT NULL, -- Reference to the user responsible for adding the facility
    CONSTRAINT FkFacilityServiceTypeID FOREIGN KEY (BranchId) REFERENCES [Branch] (branchId), -- Foreign key relationship with the Branch table
    CONSTRAINT FkFacilityUserPersonID FOREIGN KEY (UserPersonId) REFERENCES [User] (PersonId) -- Foreign key relationship with the User table
);

-- Creating the Invoice table to store information about customer invoices
CREATE TABLE [Invoice](
    InvoiceId INT IDENTITY(1,1) PRIMARY KEY, -- Unique identifier for each invoice
    CustomerId INT NOT NULL, -- Reference to the customer associated with the invoice
    DueDate SMALLDATETIME NOT NULL, -- Due date for the invoice payment
    BillAmount MONEY NOT NULL, -- Total bill amount in the invoice
    Balance MONEY NOT NULL, -- Remaining balance to be paid
    InsertDate SMALLDATETIME NOT NULL CONSTRAINT DfInvoiceInsertDate DEFAULT(GETDATE()), -- Date when the invoice record is inserted
    UserPersonId INT NOT NULL, -- Reference to the user responsible for generating the invoice
    CONSTRAINT FkInvoiceCustomerID FOREIGN KEY (CustomerID) REFERENCES [Customer] (PersonID), -- Foreign key relationship with the Customer table
    CONSTRAINT FkInvoiceUserPersonID FOREIGN KEY (UserPersonId) REFERENCES [User] (PersonId) -- Foreign key relationship with the User table
);

-- Creating the Transaction table to store information about transactions (e.g., room service transactions)
CREATE TABLE [Transaction](
    TransactionId INT IDENTITY(1,1) PRIMARY KEY, -- Unique identifier for each transaction
    RoomId INT NOT NULL, -- Reference to the room associated with the transaction
    CustomerId INT NOT NULL, -- Reference to the customer associated with the transaction
    ServiceTypeID INT NOT NULL, -- Reference to the type of service in the transaction
    ServiceID INT NOT NULL, -- Reference to the specific service in the transaction
    Quantity VARCHAR(100) NOT NULL, -- Quantity of the service or product in the transaction
    Amount MONEY NOT NULL, -- Total amount for the transaction
    InvoiceID INT, -- Reference to the invoice associated with the transaction
    InsertDate SMALLDATETIME NOT NULL CONSTRAINT DfTransactionInsertDate DEFAULT(GETDATE()), -- Date when the transaction record is inserted
    UserPersonId INT NOT NULL, -- Reference to the user responsible for the transaction
    CONSTRAINT FkTransactionRoomID FOREIGN KEY (RoomID) REFERENCES [Room] (RoomID), -- Foreign key relationship with the Room table
    CONSTRAINT FkTransactionCustomerID FOREIGN KEY (CustomerID) REFERENCES [Customer] (PersonID), -- Foreign key relationship with the Customer table
    CONSTRAINT FkTransactionUserPersonID FOREIGN KEY (UserPersonId) REFERENCES [User] (PersonId), -- Foreign key relationship with the User table
    CONSTRAINT FkTransactionServiceTypeID FOREIGN KEY (ServiceTypeId) REFERENCES [ServiceType] (ServiceTypeId), -- Foreign key relationship with the ServiceType table
    CONSTRAINT FkTransactionInvoiceID FOREIGN KEY (InvoiceId) REFERENCES [Invoice] (InvoiceId) -- Foreign key relationship with the Invoice table
);

-- Creating the Payment table to store information about payments made by customers
CREATE TABLE [Payment](
    PaymentId INT IDENTITY(1,1) PRIMARY KEY, -- Unique identifier for each payment
    Amount MONEY NOT NULL, -- Amount of the payment
    InvoiceID INT NOT NULL, -- Reference to the invoice associated with the payment
    InsertDate SMALLDATETIME NOT NULL CONSTRAINT DfPaymentInsertDate DEFAULT(GETDATE()), -- Date when the payment record is inserted
    UserPersonId INT NOT NULL, -- Reference to the user responsible for processing the payment
    CONSTRAINT FkPaymentInvoiceID FOREIGN KEY (InvoiceID) REFERENCES [Invoice] (InvoiceID), -- Foreign key relationship with the Invoice table
    CONSTRAINT FkPaymentUserPersonID FOREIGN KEY (UserPersonId) REFERENCES [User] (PersonId) -- Foreign key relationship with the User table
);

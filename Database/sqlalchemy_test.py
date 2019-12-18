from pprint import pprint

from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:////web/Sqlite-Data/example.db')

# this loads the sqlalchemy base class
Base = declarative_base()


# Setting up the classes that create the record objects and define the schema

class Customer(Base):
    __tablename__ = 'customer'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    address = Column(String(250), nullable=False)
    town = Column(String(250), nullable=False)


class Item(Base):
    __tablename__ = 'item'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    name = Column(String(250))
    cost_price = Column(Integer, primary_key=True)
    selling_price = Column(Integer, primary_key=True)
    quantity = Column(Integer, primary_key=True)


# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Insert a Person in the person table
new_person1 = Customer(name='Keith')
# this adds person to the session
session.add(new_person1)

new_person2 = Customer(name='Joe')
session.add(new_person1)

new_person3 = Customer(name='Steve')
session.add(new_person1)
# commit saves the changes
session.commit()

# Insert an Address in the address table using a loop

items = {
    Item('Chair', 9, 10, 5),
    Item('Table', 15, 17 , 10),
}

# Loop through addresses and commit them to the database
for Item in items:
    session.add(Item)
    session.commit()

# joins Person on Address
all_people = session.query(Customer).join(Customer).all()

# Accessing a person with their address, You have to loop the addresses property and remember it was added by the
# backref on the addresses class
for person in all_people:
    # use the __dict__ magic method to have the object print it's properties
    pprint(person.__dict__)
    for address in person.addresses:
        pprint(address.__dict__)

# Retrieving the inverse of the relationship.  Notice I reverse the Person and Address to load the Address table
all_addresses = session.query(Item).join(Customer).all()
for address in all_addresses:
    # showing how to use the print function with printing text and data at the same time easily
    print(f'{address.person.name} has a postal code of {address.post_code}')
from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.types import PickleType
import datetime


engine = create_engine('sqlite:///student.db', echo=True)
Base = declarative_base()
 
########################################################################
class Student(Base):
    """"""
    __tablename__ = "student"
 
    id = Column(Integer, primary_key=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    university = Column(String)

    #----------------------------------------------------------------------
    def __init__(self, username, firstname, lastname, university):
        """"""
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.university = university
class Play(Base):
    __tablename__ = "play1"

    play_id=Column(Integer, primary_key=True)
    sp=Column(String)
    id=Column(Integer, ForeignKey('student.id'))
    #student = relationship("Student", back_populates="play1")
    def __init__(self,id,sp):
        """"""
        self.id=id
        self.sp=sp

#Student.play1 = relationship("Play", order_by=Play.id, back_populates="student")
 

class Foo(Base):
    __tablename__ = 'foo'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    array = Column(PickleType)
    def __init__(self, id, name, array):
        """"""
        self.id=id
        self.name = name
        self.array=array

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                                self.name, self.fullname, self.nickname)
								
class Address(Base):
     __tablename__ = 'addresses'
     id = Column(Integer, primary_key=True)
     email_address = Column(String, nullable=False)
     user_id = Column(Integer, ForeignKey('users.id'))

     #user = relationship("User", back_populates="addresses")

     def __repr__(self):
         return "<Address(email_address='%s')>" % self.email_address

#User.addresses = relationship(
#     "Address", order_by=Address.id, back_populates="user")

       

# create tables
Base.metadata.create_all(engine)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# Create objects  
user = Student("james","James","Boogie","MIT")
#session.add(user)

user = Student("lara","Lara","Miami","UU")
#session.add(user)

user = Student("eric","Eric","York","Stanford")
#session.add(user)

foo1=Foo(1,"Anik",[1,2,34])
#session.add(foo1)

foo2=Foo(3,"Rifat",[2,3,4,5])
#session.add(foo2)

##sp1=Play(1,"Cricket")
##session.add(sp1)
##
##sp1=Play(2,"Football")
##session.add(sp2)
#jack = User(name='jack', fullname='Jack Bean', nickname='gjffdd')

#jack.addresses = [Address(email_address='jack@google.com'),
#                  Address(email_address='j25@yahoo.com')]
#session.add(jack)

for student in session.query(Student).order_by(Student.id):
    print (student.firstname, student.lastname)

for student in session.query(Student).filter(Student.firstname == 'Eric'):
    print (student.firstname, student.lastname)

for foo in session.query(Foo).filter(Foo.name=='Anik'):
    print (foo.array)

print(session.query(User).join(Address).filter(Address.email_address=='jack@google.com').all())

# commit the record the database
session.commit()

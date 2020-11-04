from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.types import PickleType
import datetime

engine = create_engine('sqlite:///AIR_RESERVATION_SYSTEM_ORM.db', echo=True)
Base = declarative_base()

#Entities
class Countryy(Base):
    """"""
    __tablename__ = "country"
 
    country_id = Column(String, primary_key=True)
    country_name = Column(String, primary_key=True)
    population = Column(Integer, nullable=False)
    
class Airlinee(Base):
    """"""
    __tablename__ = "airline"
 
    airline_id = Column(String, primary_key=True)
    airline_name = Column(String, primary_key=True)
    airline_type = Column(String, nullable=False)

class AeroPlanee(Base):
    """"""
    __tablename__ = "aeroplane"
 
    aeroplane_id = Column(String, primary_key=True)
    seat_number = Column(Integer, nullable=False)

class PNRR(Base):
    """"""
    __tablename__ = "pnr"
 
    passenger_name = Column(String, nullable=False)
    contact_info = Column(PickleType, primary_key=True)
    passport_number=Column(Integer, primary_key=True)
    date_of_expiry=Column(PickleType)

class PSSRR(Base):
    """"""
    __tablename__ = "pssr"
 
    service_id = Column(String, primary_key=True)
    service_name = Column(String, primary_key=True)

class Airportt(Base):
    """"""
    __tablename__ = "airport"
 
    airport_id = Column(String, primary_key=True)
    airport_name = Column(String, primary_key=True)
    airport_type=Column(String, nullable=False)
    number_of_runways=Column(Integer, nullable=False)

#Weak Entity
class Seatt(Base):
    """"""
    __tablename__ = "seat"
 
    seat_id = Column(String, primary_key=True)
    seat_class = Column(String, nullable=False)
    seat_price=Column(Integer, nullable=False)
    booking_conditions=Column(PickleType, nullable=False)
    aeroplane_id=Column(String, ForeignKey('aeroplane.aeroplane_id'))

class Flightt(Base):
    """"""
    __tablename__ = "flight"
 
    flight_id = Column(String, primary_key=True)
    source_airport_id = Column(String, ForeignKey('airport.airport_id'))
    destination_airport_id = Column(PickleType,ForeignKey('airport.airport_id'))
    flight_date_time=Column(String, nullable=False)
    distance=Column(PickleType, nullable=False)
    flight_price=Column(PickleType, nullable=False)
    aeroplane_id=Column(String, ForeignKey('aeroplane.aeroplane_id'))

class Tickett(Base):
    """"""
    __tablename__ = "ticket"
 
    ticket_id = Column(String, primary_key=True)
    ticket_price=Column(Integer, nullable=False)
    ticket_type=Column(String, nullable=False)
    departure_date_time=Column(String, nullable=False)
    arrival_date_time=Column(String, nullable=False)
    source_airport_id = Column(String,ForeignKey('airport.airport_id'))
    destination_airport_id = Column(String,ForeignKey('airport.airport_id'))
    flight_id=Column(String, ForeignKey('flight.flight_id'))

#relations
class Country_Airlinee(Base):
    """"""
    __tablename__ = "country_airline"
 
    id=Column(Integer, primary_key=True)
    country_id=Column(String,ForeignKey('country.country_id'))
    country_name=Column(String,ForeignKey('country.country_name'))
    airline_id=Column(String,ForeignKey('airline.airline_id'))
    airline_name=Column(String,ForeignKey('airline.airline_name'))

class Airline_AeroPlanee(Base):
    """"""
    __tablename__ = "airline_aeroplane"
 
    id=Column(Integer, primary_key=True)
    aeroplane_id=Column(String, ForeignKey('aeroplane.aeroplane_id'))
    airline_id=Column(String,ForeignKey('airline.airline_id'))
    airline_name=Column(String,ForeignKey('airline.airline_name'))

class Country_Passengerr(Base):
    """"""
    __tablename__ = "country_passenger"
 
    id=Column(Integer, primary_key=True)
    country_id=Column(String,ForeignKey('country.country_id'))
    country_name=Column(String, ForeignKey('country.country_name'))
    passport_number=Column(Integer,ForeignKey('pnr.passport_number'))

class PNR_PSSRR(Base):
    """"""
    __tablename__ = "pnr_pssr"
 
    id=Column(Integer, primary_key=True)
    service_id=Column(String,ForeignKey('pssr.service_id'))
    service_name=Column(String, ForeignKey('pssr.service_name'))
    passport_number=Column(Integer,ForeignKey('pnr.passport_number'))

class Boarding_Pass(Base):
    """"""
    __tablename__ = "boarding_pass"
 
    id=Column(Integer, primary_key=True)
    airport_id=Column(String,ForeignKey('airport.airport_id'))
    ticket_id=Column(String,ForeignKey('ticket.ticket_id'))
    flight_id=Column(String,ForeignKey('flight.flight_id'))
    passport_number=Column(Integer,ForeignKey('pnr.passport_number'))

class Agentt(Base):
    """"""
    __tablename__ = "agent"
 
    license_number=Column(String,primary_key=True)
    membership_number=Column(String,primary_key=True)
    airport_id=Column(String,ForeignKey('airport.airport_id'))
    ticket_id=Column(String,ForeignKey('ticket.ticket_id'))
    passport_number=Column(Integer,ForeignKey('pnr.passport_number'))

class Ticket_Seatt(Base):
    """"""
    __tablename__ = "ticket_seat"
 
    id=Column(Integer,primary_key=True)
    aeroplane_id=Column(String,ForeignKey('seat.aeroplane_id'))
    ticket_id=Column(String,ForeignKey('ticket.ticket_id'))
    seat_id=Column(String,ForeignKey('seat.seat_id'))

# create tables
Base.metadata.create_all(engine)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()



# commit the record the database
session.commit()

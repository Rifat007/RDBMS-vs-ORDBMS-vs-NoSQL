import sqlite3
#from employee import Employee

conn = sqlite3.connect('AIR_RESERVATION_SYSTEM.db')
c = conn.cursor()


#Entities
c.execute("""CREATE TABLE IF NOT EXISTS Country (
            country_id text,
            country_name text,
            population integer NOT NULL,
            PRIMARY KEY(country_id,country_name)
           )""")

c.execute("""CREATE TABLE IF NOT EXISTS Airline (
            airline_id text,
            airline_name text,
            airline_type text NOT NULL,
            PRIMARY KEY(airline_id,airline_name)
           )""")

c.execute("""CREATE TABLE IF NOT EXISTS AeroPlane (
            aeroplane_id text PRIMARY KEY,
            seat_number integer NOT NULL
           )""")

c.execute("""CREATE TABLE IF NOT EXISTS PNR (
            name text NOT NULL,
            contact_info text,
            passport_number integer,
            date_of_expiry text,
            PRIMARY KEY(contact_info,passport_number)
           )""")

c.execute("""CREATE TABLE IF NOT EXISTS PSSR (
            service_id text,
            service_name text,
            PRIMARY KEY(service_id,service_name)
           )""")

c.execute("""CREATE TABLE IF NOT EXISTS Airport (
            airport_id text,
            airport_name text,
            airport_type text NOT NULL,
            number_of_runways integer NOT NULL,
            PRIMARY KEY(airport_id,airport_name)
           )""")

#Weak Entity
c.execute("""CREATE TABLE IF NOT EXISTS Seat (
            seat_id text PRIMARY KEY,
            class text NOT NULL,
            seat_price integer NOT NULL,
            booking_conditions NOT NULL,
            aeroplane_id text,
            FOREIGN KEY(aeroplane_id) REFERENCES AeroPlane(aeroplane_id)
           )""")

c.execute("""CREATE TABLE IF NOT EXISTS Flight (
            flight_id text PRIMARY KEY,
            source_airport_id text NOT NULL,
            destination_airport_id text NOT NULL,
            flight_date_time text NOT NULL,
            distance REAL NOT NULL,
            flight_price integer NOT NULL,
            aeroplane_id text,
            FOREIGN KEY(aeroplane_id) REFERENCES AeroPlane(aeroplane_id),
            FOREIGN KEY(source_airport_id) REFERENCES Airport(airport_id),
            FOREIGN KEY(destination_airport_id) REFERENCES Airport(airport_id)
           )""")

c.execute("""CREATE TABLE IF NOT EXISTS Ticket (
            ticket_id text PRIMARY KEY,
            ticket_price integer NOT NULL,
            ticket_type text NOT NULL,
            departure_date_time text NOT NULL,
            arrival_date_time text NOT NULL,
            source_airport_id text NOT NULL,
            destination_airport_id text NOT NULL,
            flight_id text,
            FOREIGN KEY(source_airport_id) REFERENCES Airport(airport_id),
            FOREIGN KEY(destination_airport_id) REFERENCES Airport(airport_id),
            FOREIGN KEY(flight_id) REFERENCES Flight(flight_id)
           )""")

#relations
c.execute("""CREATE TABLE IF NOT EXISTS Country_Airline (
            country_id text,
            country_name text,
            airline_id text,
            airline_name text,
            FOREIGN KEY(country_id,country_name) REFERENCES Country(country_id,country_name),
            FOREIGN KEY(airline_id,airline_name) REFERENCES Airline(airline_id,airline_name)
           )""")

c.execute("""CREATE TABLE IF NOT EXISTS Airline_AeroPlane (
            aeroplane_id text,
            airline_id text,
            airline_name text,
            FOREIGN KEY(aeroplane_id) REFERENCES AeroPlane(aeroplane_id),
            FOREIGN KEY(airline_id,airline_name) REFERENCES Airline(airline_id,airline_name)
           )""")

c.execute("""CREATE TABLE IF NOT EXISTS Country_Passenger (
            country_id text,
            country_name text,
            passport_number integer,
            FOREIGN KEY(passport_number) REFERENCES PNR(passport_number),
            FOREIGN KEY(country_id,country_name) REFERENCES Country(country_id,country_name)
           )""")

c.execute("""CREATE TABLE IF NOT EXISTS PNR_PSSR (
            service_id text,
            service_name text,
            passport_number integer,
            FOREIGN KEY(passport_number) REFERENCES PNR(passport_number),
            FOREIGN KEY(service_id,service_name) REFERENCES PSSR(service_id,service_name)
           )""")

c.execute("""CREATE TABLE IF NOT EXISTS Boarding_Pass (
            passport_number integer,
            airport_id text,
            ticket_id text,
            flight_id text,
            FOREIGN KEY(passport_number) REFERENCES PNR(passport_number),
            FOREIGN KEY(airport_id) REFERENCES Airport(airport_id),
            FOREIGN KEY(ticket_id) REFERENCES Ticket(ticket_id),
            FOREIGN KEY(flight_id) REFERENCES Flight(flight_id)
           )""")

c.execute("""CREATE TABLE IF NOT EXISTS Agent (
            license_number text,
            membership_number text,
            ticket_id text,
            passport_number integer,
            PRIMARY KEY(license_number,membership_number),
            FOREIGN KEY(passport_number) REFERENCES PNR(passport_number),
            FOREIGN KEY(ticket_id) REFERENCES Ticket(ticket_id)
           )""")

c.execute("""CREATE TABLE IF NOT EXISTS Ticket_Seat (
            ticket_id text,
            seat_id text,
            aeroplane_id text,
            FOREIGN KEY(ticket_id) REFERENCES Ticket(ticket_id),
            FOREIGN KEY(seat_id) REFERENCES Seat(seat_id),
            FOREIGN KEY(aeroplane_id) REFERENCES Seat(aeroplane_id)
           )""")

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})

#emp_1 = Employee('John', 'Doe', 80000)
#emp_2 = Employee('Jane', 'Doe', 90000)

#insert_emp(emp_1)
#insert_emp(emp_2)

#emps = get_emps_by_name('Doe')
#print(emps)

#update_pay(emp_2, 95000)
#remove_emp(emp_1)

#emps = get_emps_by_name('Doe')
#print(emps)

#c.execute("SELECT * FROM employees")
#out=c.fetchall()

#for i in out:
#    print("First_Name: "+i[0]+" Last_Name: "+i[1]+" Position: ",i[2])

conn.commit()
conn.close()

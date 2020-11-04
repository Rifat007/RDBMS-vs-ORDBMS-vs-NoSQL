import sqlite3


#Database creation
conn = sqlite3.connect('EMPLOYEE.db')

c = conn.cursor()

#Creating table
##c.execute("""CREATE TABLE employees (
##            first text,
##            last text,
##            pay integer
##           )""")


#Function for insertion
def insert_emp(emp_first,emp_last,emp_pay):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_first, 'last': emp_last, 'pay': emp_pay})


#Function for query
def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()


#Function for update
def update_pay(emp_first,emp_last, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp_first, 'last': emp_last, 'pay': pay})


#Function for remove 
def remove_emp(emp_first,emp_last):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp_first, 'last': emp_last})



##insert_emp('John','Doe',80000)
##insert_emp('Jane', 'Doe', 90000)

#emps = get_emps_by_name('Doe')
#print(emps)

#update_pay('Jane', 'Doe', 95000)
#remove_emp('Jane', 'Doe')

#emps = get_emps_by_name('Doe')
#print(emps)

c.execute("SELECT * FROM employees")
out=c.fetchall()

for i in out:
    print("First_Name: "+i[0]+" Last_Name: "+i[1]+" Position: ",i[2])

conn.commit()
conn.close()

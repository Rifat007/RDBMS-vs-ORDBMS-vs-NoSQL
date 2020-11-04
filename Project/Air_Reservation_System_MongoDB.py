from pymongo import MongoClient
from random import randint

client = MongoClient('localhost',port=27017)
db=client.AIR_RESERVATION_SYSTEM_MONGODB6

##
flight1={'flight_id':"fl1",
         'avail_seats':["A1","A2","A3","B1","B2","B3"],
         'airline':"AA Air",
         'src_aport':"S",
         'dest_aport':["D1","D2","D3"],
         'dep_date':"23/9/19",
         'dep_time':"12:00",
         'arr_date':["23/9/19","24/9/19","24/9/19"],
         'arr_time':["18:30","2:30","4:30"],
         'flight_price':["200","500","600"],
         'passengers':["pp_221","pp_333"]}

flight2={'flight_id':"fl2",
         'avail_seats':["A4","A5","A6","B1","B2","B3"],
         'airline':"AA Air",
         'src_aport':"S",
         'dest_aport':["D1","D2","D4"],
         'dep_date':"23/9/19",
         'dep_time':"13:00",
         'arr_date':["23/9/19","24/9/19","24/9/19"],
         'arr_time':["18:30","2:30","4:30"],
         'flight_price':["250","500","600"],
         'passengers':["pp_223","pp_343"]}

flight3={'flight_id':"fl3",
         'avail_seats':["A1","A6","A7","B1","B4","B5"],
         'airline':"AADD Air",
         'src_aport':"S",
         'dest_aport':["D3","D4","D7"],
         'dep_date':"24/9/19",
         'dep_time':"13:30",
         'arr_date':["24/9/19","25/9/19","25/9/19"],
         'arr_time':["16:30","4:30","5:30"],
         'flight_price':["100","500","600"],
         'passengers':["pp_121","pp_133"]}

result1=db.flights.insert_one(flight1)
result2=db.flights.insert_one(flight2)
result3=db.flights.insert_one(flight3)

print("Available seats of a flight")
for f in db.flights.find({'flight_id':"fl1"},{'_id':False, 'flight_id':True, 'avail_seats':True}):
    print(f)

print("\n\nFligt list & Departure Time")
for f in db.flights.find({},{'_id':False, 'flight_id':True, 'dep_date':True,'dep_time':True}):
    print(f)

print("\n\nFligt list & Arrival Time")
print("Flight1")
for f in db.flights.find({'flight_id':"fl1"},{'_id':False,'arr_time':True}):
    print(f)
for f in db.flights.find({'flight_id':"fl1"},{'_id':False,'arr_date':True}):
    print(f)
for f in db.flights.find({'flight_id':"fl1"},{'_id':False,'dest_aport':True}):
    print(f)

print("\nFlight2")
for f in db.flights.find({'flight_id':"fl2"},{'_id':False,'arr_time':True}):
    print(f)
for f in db.flights.find({'flight_id':"fl2"},{'_id':False,'arr_date':True}):
    print(f)
for f in db.flights.find({'flight_id':"fl2"},{'_id':False,'dest_aport':True}):
    print(f)

print("\nFlight3")
for f in db.flights.find({'flight_id':"fl3"},{'_id':False,'arr_time':True}):
    print(f)
for f in db.flights.find({'flight_id':"fl3"},{'_id':False,'arr_date':True}):
    print(f)
for f in db.flights.find({'flight_id':"fl3"},{'_id':False,'dest_aport':True}):
    print(f)

print("\n\nOn board passengers")
for f in db.flights.find({'dep_date':"23/9/19",'airline':"AA Air",'flight_id':"fl1"},{'_id':False,'dep_date':True,'airline':True,'flight_id':True,'passengers':True}):
    print(f)

##
passenger1={'pass_num':"pp_221",
            'name':"Mr.A",
            'country':"BD",
            'service':["s1","s2"],
            'flight_id':["fl1"],
            'seat_no':["A4"],
            'dept_date':["23/9/19"],
            'dept_time':["12:00"],
            'src_aport':["S"],
            'dest_aport':["D1"]}

p1=db.passengers.insert_one(passenger1)

for pp in db.passengers.find():
    print(pp)

passport_inp=input("\n\nGive passport number: ")
nm=input("\nName: ")
cntry=input("\nCountry: ")
total_ser=input("\nTotal_Service: ")
print("\nGive service id")
ser=[]
for i in range(0,int(total_ser)):
    ser.append(input())

print("\n############# New Booking #################")

dp_dt=input("\nDeparture Date: ")
src=input("\nSource Airport: ")
dest=input("\nDestination Airport: ")
for f in db.flights.find({'dep_date':dp_dt,'src_aport':src,'dest_aport':{'$eq':dest}},{'_id':False,'flight_id':True,'avail_seats':True,'dep_time':True}):
    print(f)


fl_id=input("\nFlight_id: ")
st_no=input("\nSeat_No: ")
dp_tm=input("\nDeparture Time: ")

cnt=db.passengers.find({'pass_num':passport_inp}).count()
print(cnt)

db.flights.update({'flight_id':fl_id},{ '$pull':{'avail_seats': st_no} } )
db.flights.update({'flight_id':fl_id},{'$push':{'passengers': passport_inp} } )

print("Available seats of a flight")
for f in db.flights.find({'flight_id':fl_id},{'_id':False, 'flight_id':True, 'avail_seats':True}):
    print(f)

if(cnt>0):
    db.passengers.update({'pass_num':passport_inp},{'$push':{'flight_id':fl_id}})
    db.passengers.update({'pass_num':passport_inp},{'$push':{'seat_no':st_no}})
    db.passengers.update({'pass_num':passport_inp},{'$push':{'dept_date':dp_dt}})
    db.passengers.update({'pass_num':passport_inp},{'$push':{'dept_time':dp_tm}})
    db.passengers.update({'pass_num':passport_inp},{'$push':{'src_aport':src}})
    db.passengers.update({'pass_num':passport_inp},{'$push':{'dest_aport':dest}})
    for i in range(0,int(total_ser)):
        db.passengers.update({'pass_num':passport_inp},{'$push':{'service':ser[i]}})
else:
    passenger1={'pass_num':passport_inp,
            'name':nm,
            'country':cntry,
            'service':[ser[0]],
            'flight_id':[fl_id],
            'seat_no':[st_no],
            'dept_date':[dp_dt],
            'dept_time':[dp_tm],
            'src_aport':[src],
            'dest_aport':[dest]}
    p1=db.passengers.insert_one(passenger1)
    for i in range(1,int(total_ser)):
        db.passengers.update({'pass_num':passport_inp},{'$push':{'service':ser[i]}})
    
for pp in db.passengers.find():
    print(pp)


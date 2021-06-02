"""
Bus Seat Registration Program
"""
class Bus:
    is_avail = False
    def __init__(self,bus_bo,registration_name,conductor_name,driver_name,total_seats,seats_booked):
        self.registration_name = registration_name
        self.conductor_name = conductor_name
        self.driver_name = driver_name
        self.total_seats = total_seats
        self.seats_booked = seats_booked
        self.bus_no = bus_bo

    def print_bus_details(self):
        print("Bus No.:",self.bus_no,"Driver Name:",self.driver_name,"Conductor Name:",self.conductor_name)
        print("Total Seats:",self.total_seats,"Seats Booked:",self.seats_booked)
        print("Available Seats:",self.total_seats-self.seats_booked,"\n")

    def is_seat_available(self,no_of_seats):
        if self.total_seats-self.seats_booked >= no_of_seats:
            self.total_seats -= self.seats_booked - no_of_seats
            self.is_avail =  True
        else:
            self.is_avail =  False

    def book_seat(self,no_of_seats):
        if self.is_avail == True:
            print("Seats Booked")
        else:
            print("Requested no of seats not available")

obj1 = Bus("TN101","JOE","ADAM","JOHN",25,13)
obj1.print_bus_details()
obj1.book_seat(25)

"""
Output:
/GitHub/talentpy-Assgn5/Bus.py

Bus No.: TN101 Driver Name: JOHN Conductor Name: ADAM
Total Seats: 25 Seats Booked: 13
Available Seats: 12
Requested no of seats not available
"""
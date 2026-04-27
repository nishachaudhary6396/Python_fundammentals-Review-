class NoSeatAvailableException(Exception):
    pass

class Flight:    #store seats
    def __init__(self,flight_no,departure,arrival,totalSeats):
        self.__flight_no = flight_no
        self.__departure = departure
        self.__arrival = arrival
        self.__totalSeats = totalSeats
        self.__bookedSeats = 0
        
    def get_seats(self):
        return self.__totalSeats - self.__bookedSeats
    
    
    def get_flight_no(self):
        return self.__flight_no
    
    def book_seat(self):
        if self.get_seats() <= 0:
            raise NoSeatAvailableException("No seats Available")
        else:
            self.__bookedSeats += 1
        
class Passenger:
    def __init__(self,name):
        self.name = name
    
    def book_flight(self,flight):   
        flight.book_seat()
        print(f"{self.name} booked {flight.get_flight_no()}")

class EconomyPassenger(Passenger):      #book seat if available
    def book_flight(self,flight):
        if flight.get_seats() > 0:
            super().book_flight(flight)
        else:
            raise NoSeatAvailableException(f"No seat for {self.name}")  # if no seat is available
        
class BusinessPassenger(Passenger):
    def book_flight(self,flight):
        print("Priority booking")
        super().book_flight(flight)

flight = Flight("Indigo","Agra","Mumbai",2)

passengers = [
    EconomyPassenger("Nisha"),
    BusinessPassenger("Rahul"),
    EconomyPassenger("Aman")
]

for p in passengers:
    try:
        p.book_flight(flight)
    except NoSeatAvailableException as e:
        print(e)
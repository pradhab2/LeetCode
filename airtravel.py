""" Model for Aircraft flights """

import mysql.connector as db
import config

db_server = config.db_server
db_user = config.db_usr
db_pwd = config.db_pwd
db_nm = config.db_nm


class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_of_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return range(1, self._num_of_rows + 1), "ABCDEFGHJK"[:self._num_seats_per_row]


# a=Aircraft("G-EUPT","Airbus A319",num_rows=22, num_seats_per_row=6)
# a.seating_plan()
# (range(1, 23), 'ABCDEF')


class Flight:
    """ A flight with a particular passenger aircraft
    Flight Number will have first two letters alphabet in upper case and last three digit numeric
    e.g. BA758 """

    def __init__(self, fltNumber, aircraft):  # Here Aircraft is a class
        if not fltNumber[:2].isalpha():
            raise ValueError("Invalid airline code %s" % fltNumber)

        if not fltNumber[:2].isupper():
            raise ValueError("Invalid airline code %s" % fltNumber)

        if not fltNumber[2:].isdigit() and int(fltNumber[2:] <= 9999):
            raise ValueError("Invalid route number %s" % fltNumber)

        self._fltNumber = fltNumber
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()  # rows are list of rows and seats is a String = ABCDEFGHJ
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def aircraftModel(self):
        return self._aircraft.model()

    def aircraftRegdNum(self):
        return self._aircraft.registration()

    def fltNumber(self):
        return self._fltNumber

    def allocate_seat(self, seatnum, passenger_nm):
        """ Allocate seat number to Passenger

        Args:
            seatnum : A seat designator such as '12C' or '21F'.
            parssenger_name: The passenger name
        Raises:
            ValueError: If seat is unavailable or invalid
        """
        row, letter = self._parse_seat(seatnum)

        if self._seating[row][letter] is not None:
            raise ValueError("The seat %s is already occupied" % seatnum)

        self._seating[row][letter] = passenger_nm

    def _parse_seat(self, seatnum):
        rows, seat_letter = self._aircraft.seating_plan()

        letter = seatnum[-1]  # last letter in the seatnum
        if letter not in seat_letter:
            raise ValueError("Invalid seat letter %s" % letter)

        rownum = seatnum[:-1]
        try:
            row = int(rownum)
        except ValueError:
            raise ValueError("Invalid seat number %s" % rownum)

        if row not in rows:
            raise ValueError("Invalid row number %s" % rownum)

        return row, letter

    def num_available(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)

    def make_boarding_cards(self, card_printer):
        for passenger_nm, seat_num in sorted(self._get_ocupied_seats()):
            card_printer(passenger_nm, seat_num, self.fltNumber(), self.aircraftModel())

    def log_booking(self):
        record = []
        for passenger_nm, seat_num in self._get_ocupied_seats():
            #print("passenger name: %s and seat is %s" % (passenger_nm, seat_num ))
            record.append(tuple((passenger_nm, seat_num, self.fltNumber(), self.aircraftModel())))
            #record.append(data)

        print(record)
        insert_booking_info = 'INSERT INTO parking.flight_seat_alloc (Passenger_nm, Seat_num, Flight_num, ' \
                              'Flight_Model) VALUES( %s,%s,%s,%s) '

        conn = db.connect(host=db_server, user=db_user, passwd=db_pwd, db=db_nm)
        cursor = conn.cursor()
        cursor.executemany(insert_booking_info, record)
        print(cursor.rowcount, "record inserted.")
        conn.commit()
        cursor.close()
""" from airtravel import make_flight
m=make_flight()
m.log_booking()
[('Balaram', '1A', 'BS453', 'AirbusA319'), ('Ramesh', '2B', 'BS453', 'AirbusA319'), ('Kailash', '2C', 'BS453', 'AirbusA319'), ('Harish', '3C', 'BS453', 'AirbusA319')]
4 record inserted. 
"""

    def _get_ocupied_seats(self):
        """ An iterable series of passenger seating locations """

        row_number, seat_letters = self._aircraft.seating_plan()
        for row in row_number:
            for letter in seat_letters:
                passenger_nm = self._seating[row][letter]
                if passenger_nm is not None:
                    # yield passenger_nm, "%s%s" % (row, letter)
                    yield passenger_nm, str(row) + letter

    def relocate_passenger(self, fromSeat, toSeat):
        """ Relocate passenger to different seat.
            Args:
                fromSeat: the existing seat designator for the passenger to be moved
                toSeat: the new seat designator
        """
        fromRow, fromLetter = self._parse_seat(fromSeat)
        # print("The value of fromRow is: %s and fromLetter is: %s" % (fromRow, fromLetter) )
        if self._seating[fromRow][fromLetter] is None:
            raise ValueError("No passenger to relocate the seat %s" % fromSeat)

        toRow, toLetter = self._parse_seat(toSeat)
        if self._seating[toRow][toLetter] is not None:
            raise ValueError("Seat %s is already occupied" % toSeat)

        # print("The value of fromRow , fromLetter is: %s" % (self._seating[fromRow][fromLetter]))
        # print("The value of toRow , toLetter is: %s" % (self._seating[toRow][toLetter]))

        self._seating[toRow][toLetter] = self._seating[fromRow][fromLetter]
        self._seating[fromRow][fromLetter] = None

    def db_insert(self):
        insert_booking_info = 'INSERT INTO parking.flight_seat_alloc (Passenger_nm, Flight_num, Flight_Model,' \
                                   'Seat_num) VALUES( %s,%s,%s,%s) '
        print(insert_booking_info)

        conn = db.connect(host=db_server, user=db_user, passwd=db_pwd, db=db_nm)
        cursor = conn.cursor()
        cursor.execute(insert_booking_info, ('Jhonny', 'AI345', 'Airbus559', '9A'))
        print(cursor.rowcount, "record inserted.")
        conn.commit()
        cursor.e
        cursor.close()


"""
from airtravel import make_flight
f = make_flight()

f.relocate_passenger('1A','3A')

"""

"""
# >>> f=Flight("BS453",Aircraft("G-EUPT","Airbus A319",num_rows=22, num_seats_per_row=6))

# >>> f.aircraftModel()
# >>> 'Airbus A319'
# f.fltNumber()
# 'BS453'
# f._seating
# [None, {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None}, {'A': None, 'B': None, .........]
# from pprint import pprint as pp
# pp(f._seating)
#f._seating[1]
#{'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None}
#f._seating[1]['B']
#f._seating[1]['B']='Balaram'
#f._seating[1]['B']
#'Balaram'


runfile('/Users/balarampradhan/Documents/PycharmProjects/venv/src/airtravel.py', wdir='/Users/balarampradhan/Documents/PycharmProjects/venv/src')
f=Flight("BS453",Aircraft("G-EUPT","Airbus A319",num_rows=22, num_seats_per_row=6))
f.allocate_seat("1A","Balaram")

f._seating[1]['A']
'Balaram'

f.allocate_seat("1C","Harish")

f._seating
[None, {'A': 'Balaram', 'B': None, 'C': 'Harish', 'D': None, 'E': None, 'F': None},.......]


f.num_available()
132
f.allocate_seat("2A","Harish")
f.num_available()
131

"""


def console_card_printer(passenger_name, seat_num, flight_num, aircraft_model):
    output = "| Name: %s " % passenger_name + \
             "  Seat: %s" % seat_num + \
             "  Flight: %s" % flight_num + \
             "  Aircraft Type: %s" % aircraft_model + \
             " |"
    banner = "+" + "_" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)
    print()


def make_flight():
    f = Flight("BS453", Aircraft("G-EUPT", "AirbusA319", num_rows=10, num_seats_per_row=6))
    f.allocate_seat('1A', 'Balaram')
    f.allocate_seat('2B', 'Ramesh')
    f.allocate_seat('3C', 'Harish')
    f.allocate_seat('2C', 'Kailash')
    return f


"""
from airtravel import make_flight
f = make_flight()
f.num_available()
56
from pprint import pprint as pp
pp(f._seating)

f._seating[1]['A']
'Balaram'

"""

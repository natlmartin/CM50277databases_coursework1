# Asks user to input flight details and parses the input to generate an UPDATE statement to create new records in the flights and flight_schedule tables
# Currently generates error "Error, transaction has rolled back execute() argument 1 must be str, not tuple"
def add_flight(conn):
    cursor = conn.cursor()
    try: 
        conn.execute("BEGIN TRANSACTION")
        # Generate new ids to ensure they are unique to meet primary key constraints 
        cursor.execute("SELECT MAX(schedule_id) FROM flight_schedule;")
        new_schedule_id = cursor.fetchone()[0] + 1
        cursor.execute("SELECT MAX(flight_id) FROM flights;")
        new_flight_id = cursor.fetchone()[0] + 1
        flight_status = 'On Time'

        departure_airport = input("Please enter departure airport - XXX: \n")
        arrival_airport = input("Please enter arrival airport - XXX: \n")
        pilot_id = input("Please enter pilot id: \n")
        plane_id = input("Please enter plane id: \n")
        direct_flight = input("Is this a direct flight? True/False: \n")
        passenger_capacity = input("Please enter passenger capacity (integer): \n")
        ticket_price = input("Please enter ticket price - 00.00: \n")
        departure_date = input("Please enter departure date - YYYY-MM-DD: \n")
        arrival_date = input("Please enter arrival date - this must occur on or after departure_date -  YYYY-MM-DD: \n")
        departure_time = input("Please enter a departure_time - HH:MM:SS: \n")
        arrival_time = input("Please enter an arrival_time - HH:MM:SS: \n")

        add_flight = "INSERT INTO flights (flight_id, departure_airport, arrival_airport, pilot_id, schedule_id, plane_id, direct_flight, passenger_capacity, ticket_price) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (new_flight_id, departure_airport, arrival_airport, pilot_id, plane_id, direct_flight, passenger_capacity, ticket_price)

        add_flight_schedule = "INSERT INTO flight_schedule (schedule_id, flight_id, departure_date, departure_time, arrival_date, arrival_time, flight_status) VALUES (?, ?, ?, ?, ?, ?, ?)", (new_schedule_id, new_flight_id, departure_date, departure_time, arrival_date, arrival_time, flight_status)
        
        cursor.execute(add_flight)
        cursor.execute(add_flight_schedule)
        conn.commit()
        print("Database updated.")
    except Exception as e:
        conn.rollback()
        print("Error, transaction has rolled back", e)
    finally: 
        cursor.close()
    
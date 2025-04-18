import sqlite3

conn = sqlite3.connect('airline.db')
print("Connected to database.\n")
cursor = conn.cursor()

def add_flight():
    try: 
        cursor.execute("BEGIN")
        cursor.execute("SELECT MAX(schedule_id) FROM flight_schedule;")
        new_schedule_id = cursor.fetchone()[0] + 1
        cursor.execute("SELECT MAX(flight_id) FROM flights;")
        new_flight_id = cursor.fetchone()[0] + 1

        departure_airport, arrival_airport, pilot_id, plane_id, direct_flight, passenger_capacity, ticket_price, departure_date, departure_time, arrival_date, arrival_time = map(str.strip, input("Please enter departure airport, arrival airport, pilot id, plane id, direct flight, passenger capacity, ticket_price, departure date, departure time, arrival date, arrival time. Please separate each item with a comma.\n").split(","))

        add_flight = "INSERT INTO flights (flight_id, departure_airport, arrival_airport, pilot_id, schedule_id, plane_id, direct_flight, passenger_capacity, ticket_price) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (new_flight_id, departure_airport, arrival_airport, pilot_id, plane_id, direct_flight, passenger_capacity, ticket_price)

        add_flight_schedule = "INSERT INTO flight_schedule (schedule_id, flight_id, departure_date, departure_time, arrival_date, arrival_time, flight_status) VALUES (?, ?, ?, ?, ?, ?, 'On Time')", (new_schedule_id, new_flight_id, departure_date, departure_time, arrival_date, arrival_time)

        cursor.execute(add_flight)
        cursor.execute(add_flight_schedule)
        conn.commit
        print("Database updated.")
    except Exception as e:
        conn.rollback()
        print("Error, transaction has rolled back", e)
    
import sqlite3

def add_flight(conn):
    cursor = conn.cursor()
    try: 
        cursor.execute("BEGIN")
        cursor.execute("SELECT MAX(schedule_id) FROM flight_schedule;")
        new_schedule_id = cursor.fetchone()[0] + 1
        cursor.execute("SELECT MAX(flight_id) FROM flights;")
        new_flight_id = cursor.fetchone()[0] + 1

        user_selection = input("Please enter departure airport, arrival airport, pilot id, plane id, direct flight, passenger capacity, ticket_price, departure date, departure time, arrival date, arrival time. Please separate each item with a comma.\n")

        parameters = [param.strip() for param in user_selection.split(",")]

        clean_params = [
            str(parameters[0]),
            str(parameters[1]),
            int(parameters[2]),
            int(parameters[3]),
            bool(parameters[4]),
            int(parameters[5]),
            float(parameters[6]),
            str(parameters[7]),
            str(parameters[8]),
            str(parameters[9]),
            str(parameters[10])
        ]

        departure_airport, arrival_airport, pilot_id, plane_id, direct_flight, passenger_capacity, ticket_price, departure_date, departure_time, arrival_date, arrival_time = clean_params

        add_flight = "INSERT INTO flights (flight_id, departure_airport, arrival_airport, pilot_id, schedule_id, plane_id, direct_flight, passenger_capacity, ticket_price) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (new_flight_id, departure_airport, arrival_airport, pilot_id, plane_id, direct_flight, passenger_capacity, ticket_price)

        add_flight_schedule = "INSERT INTO flight_schedule (schedule_id, flight_id, departure_date, departure_time, arrival_date, arrival_time, flight_status) VALUES (?, ?, ?, ?, ?, ?, 'On Time')", (new_schedule_id, new_flight_id, departure_date, departure_time, arrival_date, arrival_time)

        cursor.execute(add_flight)
        cursor.execute(add_flight_schedule)
        conn.commit()
        print("Database updated.")
    except Exception as e:
        conn.rollback()
        print("Error, transaction has rolled back", e)
    cursor.close()
    
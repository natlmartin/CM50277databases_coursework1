## 2.2 SQL queries and database interaction 
import sqlite3

import utils

### FLIGHT RETRIEVAL ###

def flight_retrieval_queries(conn, destination, status, departure_date): 
    # Assumed from the brief that this needs to allow for a single criteria in each statement as the lab sheet specifies "destination, status OR departure date" but I have included a multiple query option in case.
    flight_retrieval_destination = "SELECT * FROM flights WHERE arrival_airport = ?;"
    flight_retrieval_status = "SELECT * FROM flight_schedule WHERE flight_status = ?;"
    flight_retrieval_departure_date = "SELECT * FROM flight_schedule WHERE departure_date > ?;"
    flight_multiple_criteria = "SELECT flights.*, flight_schedule.* FROM flights JOIN flight_schedule ON flights.flight_id = flight_schedule.flight_id WHERE flight_schedule.departure_date = ? OR flight_status = ?;" 
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(flight_retrieval_destination, (destination,))
    print("Retrieved flights matching destination: ", (destination), "\n")
    utils.format_sql_output(cursor)
    cursor.execute(flight_retrieval_departure_date, (departure_date,))
    print("Retrieved flights matching departure date: ", (departure_date), "\n")
    utils.format_sql_output(cursor)
    cursor.execute(flight_retrieval_status, (status,))
    print("Retrieved flights matching flight status: ", (status), "\n")
    utils.format_sql_output(cursor)
    cursor.execute(flight_multiple_criteria, (departure_date, status,))
    print("Retrieved flights matching departure date: ", (departure_date), "or status: ", (status), "\n")
    utils.format_sql_output(cursor)

    cursor.close()

### SCHEDULE MODIFICATION ###
def schedule_modification(conn, departure_time, departure_date, status, arrival_date): 
    update_departure_time = "UPDATE flight_schedule SET departure_time = ? WHERE departure_date = ?;"
    update_flight_status = "UPDATE flight_schedule SET flight_status = ? WHERE arrival_date = ?;"
    cursor = conn.cursor()
    cursor.execute(update_departure_time, (departure_time, departure_date,))
    print("Record updated.\n")
    cursor.execute(update_flight_status, (status, arrival_date,))
    print("Record updated.\n")
    conn.commit()
    cursor.close()

### PILOT ASSIGNMENT ###
def pilot_assignment(conn, pilot, schedule):
    assign_pilot = "UPDATE flights SET pilot_id = ? WHERE schedule_id = ?;"
    retrieve_pilot_schedule = "SELECT flights.departure_airport, flights.arrival_airport, flights.pilot_id, flight_schedule.* FROM flights LEFT JOIN flight_schedule ON flights.flight_id = flight_schedule.flight_id WHERE flights.pilot_id = ? ORDER BY flight_schedule.departure_date, flight_schedule.departure_time;"
    cursor = conn.cursor()
    cursor.execute(assign_pilot, (pilot, schedule,))
    print("Pilot ", (pilot), " assigned.\n")
    # To simulate a pilot having multiple flights 
    # cursor.execute("INSERT INTO flights (flight_id, departure_airport, arrival_airport, pilot_id, schedule_id, plane_id, direct_flight, passenger_capacity, ticket_price) VALUES (500, 'HND', 'MEX', 1, 501, 601, True, 700, 850.00);")
    # cursor.execute("INSERT INTO flight_schedule (schedule_id, flight_id, departure_date, departure_time, arrival_date, arrival_time, flight_status) VALUES (333, 500, '2025-12-01', '08:00:00', '2025-12-01', '10:00:00', 'On Time');")
    cursor.execute(retrieve_pilot_schedule, (pilot,))
    print("Schedule for pilot: ", (pilot),  "\n")
    utils.format_tuple_output(cursor)

    conn.commit()
    cursor.close()

### Destination Management ###
def retrieve_destination_information(conn, airport, runways):
    view_destination_info = "SELECT destinations.*, cities.* FROM destinations JOIN cities ON destinations.city_id = cities.city_id WHERE airport_code = ?;"
    update_destination_info = "UPDATE destinations SET total_runways = ? WHERE airport_code = ?;"
    cursor = conn.cursor()
    cursor.execute(view_destination_info, (airport,))
    utils.format_tuple_output(cursor)
    cursor.execute(update_destination_info, (runways, airport,))
    print((airport), " information updated \n")
    conn.commit()
    cursor.close() 


### Summarise Data ### 
def summarise_data(conn): 
    total_flights_per_destination = "SELECT COUNT(*) FROM flights WHERE arrival_airport = 'DXB';"
    total_flights_per_pilot = "SELECT pilot_id, COUNT(flight_id) FROM flights GROUP BY pilot_id;"
    cursor = conn.cursor()
    cursor.execute(total_flights_per_destination)
    print("Total flights for destination = ", cursor.fetchone()[0])
    cursor.execute(total_flights_per_pilot)
    utils.format_tuple_output(cursor)

    cursor.close() 
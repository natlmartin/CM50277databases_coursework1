## 2.2 SQL queries and database interaction 
import sqlite3

import utils

# FLIGHT RETRIEVAL 
flight_retrieval_destination = "SELECT * FROM flights WHERE arrival_airport = 'MEX';"
flight_retrieval_status = "SELECT * FROM flight_schedule WHERE flight_status = 'Delayed';"
flight_retrieval_departure_date = "SELECT * FROM flight_schedule WHERE departure_date > '2025-05-08';"

def flight_retrieval_queries(conn): 
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(flight_retrieval_destination)
    utils.format_sql_output(cursor)
    cursor.execute(flight_retrieval_departure_date)
    utils.format_sql_output(cursor)
    cursor.execute(flight_retrieval_status)
    utils.format_sql_output(cursor)

    cursor.close()

# SCHEDULE MODIFICATION 
update_departure_time = "UPDATE flight_schedule SET departure_time = '09:30:00' WHERE departure_date = '2025-05-01';"
update_flight_status = "UPDATE flight_schedule SET flight_status = 'On Time' WHERE arrival_date = '2025-05-02';"

def schedule_modification(): 
    conn = sqlite3.connect('airline.db')
    cursor = conn.cursor()
    cursor.execute(update_departure_time)
    print("Record updated.")
    cursor.execute(update_flight_status)
    print("Record updated.")
    conn.commit()
    cursor.close() # close cursor

# PILOT ASSIGNMENT
assign_pilot = "UPDATE flights SET pilot_id = '4' WHERE schedule_id = '3';"
retrieve_pilot_schedule = "SELECT flights.flight_id, flight_schedule.flight_id, flights.pilot_id FROM flight_schedule LEFT JOIN flights ON flight_schedule.flight_id = flights.flight_id WHERE flights.pilot_id = '1' UNION SELECT flights.flight_id, flight_schedule.flight_id, flights.pilot_id FROM flight_schedule LEFT JOIN flights ON flight_schedule.flight_id = flights.flight_id WHERE flights.pilot_id = '1';"

def pilot_assignment():
    conn = sqlite3.connect('airline.db')
    cursor = conn.cursor()
    cursor.execute(assign_pilot)
    print("Pilot assigned.")
    cursor.execute(retrieve_pilot_schedule)
    results = (cursor.fetchall())
    for row in results:
        print(row)

    conn.commit() # save changes
    cursor.close() # close cursor
    conn.close() # close connection 

    print("Database connection closed.")

# Destination Management 
view_destination_info = "SELECT * FROM destinations WHERE airport_code = 'LHR' UNION SELECT * FROM cities;"
update_destination_info = "UPDATE destinations SET total_runways = 1 WHERE airport_code = 'LHR';"

def retrieve_destination_information():
    conn = sqlite3.connect('airline.db')
    cursor = conn.cursor()
    cursor.execute(view_destination_info)
    results = (cursor.fetchall())
    for row in results:
        print(row)
    cursor.execute(update_destination_info)
    conn.commit() # save changes
    cursor.close() # close cursor
    conn.close() # close connection 

    print("Database connection closed.")

# Summarise Data 
total_flights_per_destination = "SELECT COUNT(*) FROM flights WHERE arrival_airport = 'DXB';"
total_flights_per_pilot = "SELECT COUNT(*) FROM flights WHERE pilot_id = '2';"

def summarise_data(): 
    conn = sqlite3.connect('airline.db')
    cursor = conn.cursor()
    cursor.execute(total_flights_per_destination)
    print("Total flights for destination = ", cursor.fetchone()[0])
    cursor.execute(total_flights_per_pilot)
    print("Total flights for pilot = ", cursor.fetchone()[0])

    conn.commit() # save changes
    cursor.close() # close cursor
    conn.close() # close connection 

    print("Database connection closed.")
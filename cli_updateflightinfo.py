import sqlite3

conn = sqlite3.connect('airline.db')
print("Connected to database.\n")
cursor = conn.cursor()

def update_flight_info():
    user_input = input("Which flight info would you like to update? Please choose from departure_time, flight_status: \n")
    match user_input: 
        case 'departure_time':
            # Need to add sanity checking for flight id 
            flight_id = input("Please enter the flight id this applies to: \n")
            dept_date = input("Please enter a new departure date (YYYY-MM-DD): \n")
            dept_time = input("Please enter a new departure time (HH:MM:SS): \n")
            cursor.execute("UPDATE flight_schedule SET departure_date = ?, depature_time = ? WHERE flight_id = ?", (dept_date, dept_time, flight_id,))
            conn.commit()
            results = (cursor.fetchall())
            for row in results:
                print(row)
            print("Record updated.")
        case 'flight_status':
            flight_id = input("Please enter the flight id this applies to: \n")
            new_status = input("Please enter the updated status - On Time, Cancelled, Delayed: \n")
            cursor.execute("UPDATE flight_schedule SET flight_status = ? WHERE flight_id = ?", (new_status, flight_id,))
            conn.commit()
            results = (cursor.fetchall())
            for row in results:
                print(row)
            print("Record updated.")
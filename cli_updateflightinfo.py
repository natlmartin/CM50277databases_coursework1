import utils

# User can select a parameter to update, select the flight_id for the flight to be updated and update the relevant column. 
def update_flight_info(conn):
    cursor = conn.cursor()
    user_input = input("Which flight info would you like to update? Please choose from departure_time, flight_status, price: \n")
    match user_input: 
        case 'departure_time':
            flight_id = input("Please enter the flight id this applies to: \n")
            dept_date = input("Please enter a new departure date (YYYY-MM-DD): \n")
            dept_time = input("Please enter a new departure time (HH:MM:SS): \n")
            cursor.execute("UPDATE flight_schedule SET departure_date = ?, depature_time = ? WHERE flight_id = ?", (dept_date, dept_time, flight_id,))
            conn.commit()
            print("Record updated.")
        case 'flight_status':
            flight_id = input("Please enter the flight id this applies to: \n")
            new_status = input("Please enter the updated status - On Time, Cancelled, Delayed: \n")
            cursor.execute("UPDATE flight_schedule SET flight_status = ? WHERE flight_id = ?", (new_status, flight_id,))
            conn.commit()
            print("Record updated.")
        case 'price':
            flight_id = input("Please enter the flight id this applies to: \n")
            new_price = input("Please enter the updated price: \n")
            cursor.execute("UPDATE flights SET ticket_price = ? WHERE flight_id = ?", (new_price, flight_id,))
            conn.commit()
            print("Record updated.")
    cursor.close()
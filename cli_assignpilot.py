import utils

# User can view a list of upcoming flights, select a flight_id and update the pilot_id associated with that record.
def assign_pilot(conn):
    cursor = conn.cursor()
    print("Upcoming flights: \n")
    cursor.execute("SELECT flight_id, pilot_id FROM flights;")
    utils.format_tuple_output(cursor)
    flight = input("Which of the above flights would you like to assign a pilot to? \n")
    pilot = input("Which pilot would you like to assign?\n")
    cursor.execute("UPDATE flights SET pilot_id = ? WHERE flight_id = ?", (pilot, flight,))
    conn.commit()
    cursor.close()
    print("Record updated.")

    
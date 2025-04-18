import utils

def view_pilot_schedule(conn):
    cursor = conn.cursor()
    print("Available pilots: \n")
    cursor.execute("SELECT pilot_id FROM pilots;")
    utils.format_tuple_output(cursor)
    pilot = input("Which of the above pilots would you like to view the schedule for? \n")
    cursor.execute("SELECT flights.*, flight_schedule.* FROM flights JOIN flight_schedule ON flights.flight_id = flight_schedule.flight_id WHERE pilot_id = ? ORDER BY departure_date, departure_time", (pilot,))
    utils.format_tuple_output(cursor)
    cursor.close()
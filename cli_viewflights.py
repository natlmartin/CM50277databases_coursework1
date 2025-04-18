import utils

# User can choose from multiple criteria to search for a flight and provide a parameter to print all rows matching that SELECT query. 
def view_flights(conn):
    cursor = conn.cursor()
    user_input = input("Please enter which criteria you would like to view flights by: departure_airport, arrival_airport, departure_date: \n")
    match user_input: 
        case 'departure_airport':
            dept_airport = input("Please enter an airport code: \n")
            cursor.execute("SELECT * FROM flights WHERE departure_airport = ?", (dept_airport,))
            utils.format_tuple_output(cursor)
        case 'arrival_airport':
            arr_airport = input("Please enter an airport code: \n")
            cursor.execute("SELECT * FROM flights WHERE arrival_airport = ?", (arr_airport,))
            utils.format_tuple_output(cursor)
        case 'departure_date':
            dept_date = input("Please enter a departure date (YYYY-MM-DD): \n")
            cursor.execute("SELECT * FROM flight_schedule WHERE departure_date = ?", (dept_date,))
            utils.format_tuple_output(cursor)
    conn.commit()
    cursor.close()
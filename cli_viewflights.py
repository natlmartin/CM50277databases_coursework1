import sqlite3

conn = sqlite3.connect('airline.db')
print("Connected to database.\n")
cursor = conn.cursor()

def view_flights():
    user_input = input("Please enter which criteria you would like to view flights by: departure_airport, arrival_airport, departure_date: \n")
    match user_input: 
        case 'departure_airport':
            dept_airport = input("Please enter an airport code: \n")
            cursor.execute("SELECT * FROM flights WHERE departure_airport = ?", (dept_airport,))
            results = (cursor.fetchall())
            for row in results:
                print(row)
        case 'arrival_airport':
            arr_airport = input("Please enter an airport code: \n")
            cursor.execute("SELECT * FROM flights WHERE arrival_airport = ?", (arr_airport,))
            results = (cursor.fetchall())
            for row in results:
                print(row)
        case 'departure_date':
            dept_date = input("Please enter a departure date (YYYY-MM-DD): \n")
            cursor.execute("SELECT * FROM flight_schedule WHERE departure_date = ?", (dept_date),)
            results = (cursor.fetchall())
            for row in results:
                print(row)
    conn.commit()
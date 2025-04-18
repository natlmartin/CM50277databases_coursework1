import sqlite3

conn = sqlite3.connect('airline.db')
print("Connected to database.\n")
cursor = conn.cursor()

def assign_pilot():
    print("Upcoming flights: \n")
    cursor.execute("SELECT flight_id, pilot_id FROM flights;")
    results = (cursor.fetchall())
    for row in results:
        print(row)
    flight = input("Which of the above flights would you like to assign a pilot to? \n")
    pilot = input("Which pilot would you like to assign?\n")
    cursor.execute("UPDATE flights SET pilot_id = ? WHERE flight_id = ?", (pilot, flight,))
    conn.commit()
    conn.close()
    print("Record updated.")

    
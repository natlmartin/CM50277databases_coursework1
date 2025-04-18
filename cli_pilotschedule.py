import sqlite3

conn = sqlite3.connect('airline.db')
print("Connected to database.\n")
cursor = conn.cursor()

def view_pilot_schedule():
    print("Available pilots: \n")
    cursor.execute("SELECT pilot_id FROM pilots;")
    pilot_results = (cursor.fetchall())
    for row in pilot_results:
        print(row)
    pilot = input("Which of the above pilots would you like to view the schedule for? \n")
    cursor.execute("SELECT * FROM flights WHERE pilot_id = ?", (pilot,))
    schedule_results = (cursor.fetchall())
    for row in schedule_results:
        print(row)
    conn.commit()
    conn.close()

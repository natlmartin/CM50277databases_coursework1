import sqlite3

conn = sqlite3.connect('airline.db')
print("Connected to database.\n")
cursor = conn.cursor()

def destination_info():
    cursor.execute("SELECT airport_code FROM destinations;")
    results = (cursor.fetchall())
    for row in results:
        print(row)
    destination = input("Which destination would you like to view information for? \n")
    cursor.execute("SELECT ? FROM destinations", (destination))
    results = (cursor.fetchall())
    for row in results:
        print(row)
    option = input("Would you like to update any of this information? If yes, please enter airport, city or runways. Else enter 0:\n")
    match option:
        case 'airport':
            airport = input("Which airport would you like to change this entry to? \n")
            cursor.execute("UPDATE destinations SET airport_code = ? WHERE airport_code = ?", (airport, destination,))
            conn.commit()
            conn.close()
            print("Record updated.")
        case 'city':
            city = input("Which city would you like to change this entry to? \n")
            cursor.execute("UPDATE destinations SET city_id = ? WHERE airport_code = ?", (city, destination,))
            conn.commit()
            conn.close()
            print("Record updated.")
        case 'runways':
            runways = input("How many runways would you like to change this entry to? \n")
            cursor.execute("UPDATE destinations SET runways = ? WHERE airport_code = ?", (runways, destination,))
            conn.commit()
            conn.close()
            print("Record updated.")
        case '0':
            return
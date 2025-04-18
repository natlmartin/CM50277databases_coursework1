import utils

# User can view a list of airport_codes, select an airport to view all corresponding data in the cities and destinations tables. They can then choose a parameter to update values in the selected columns for that airport.
def destination_info(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT airport_code FROM destinations;")
    utils.format_tuple_output(cursor)
    destination = input("Which destination would you like to view information for? \n")
    cursor.execute("SELECT destinations.*, cities.* FROM destinations JOIN cities ON destinations.city_id = cities.city_id WHERE destinations.airport_code = ?;", (destination,))
    utils.format_tuple_output(cursor)
    option = input("Would you like to update any of this information? If yes, please enter airport_code, city_id or total_runways. Else enter 0:\n")
    match option:
        case 'airport_code':
            airport = input("Which airport_code would you like to change this entry to? \n")
            cursor.execute("UPDATE destinations SET airport_code = ? WHERE airport_code = ?", (airport, destination,))
            conn.commit()
            conn.close()
            print("Record updated.")
        case 'city_id':
            city = input("Which city_id would you like to change this entry to? \n")
            cursor.execute("UPDATE destinations SET city_id = ? WHERE airport_code = ?", (city, destination,))
            conn.commit()
            conn.close()
            print("Record updated for airport: ", (destination))
        case 'total_runways':
            runways = input("How many runways would you like to change this entry to? \n")
            cursor.execute("UPDATE destinations SET total_runways = ? WHERE airport_code = ?", (runways, destination,))
            conn.commit()
            conn.close()
            print("Record updated for airport: ", (destination))
        case '0':
            return
## 2.3 Application development in Python 
import sqlite3

import cli_addflight
import cli_viewflights
import cli_updateflightinfo
import cli_assignpilot
import cli_pilotschedule
import cli_destinationinfo

conn = sqlite3.connect('airline.db')
print("Connected to database.\n")
cursor = conn.cursor()

def user_interface(): 

    while True: 
        print("COMMANDS:\n1 Add a flight\n2 View flights\n3 Update flight info\n4 Assign pilot\n5 View pilot schedule\n6 View/Update destination information\n0 Exit")
        command = input("Please enter the number of the command you would like to use from the above list: \n")
        match command:
            case '1':
                cli_addflight.add_flight()
            case '2':
                cli_viewflights.view_flights()
            case '3':
                cli_updateflightinfo.update_flight_info()
            case '4':
                cli_assignpilot.assign_pilot()
            case '5':
                cli_pilotschedule.view_pilot_schedule()
            case '6':
                cli_destinationinfo.destination_info()
            case '0':
                print("Happy travels!")
                break
    cursor.close() # close cursor
    conn.close() # close connection 

    print("Database connection closed.")


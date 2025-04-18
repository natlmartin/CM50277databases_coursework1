## 2.3 Application development in Python 
import sqlite3

def user_interface(): 
    conn = sqlite3.connect('airline.db')
    print("Connected to database.\n")
    cursor = conn.cursor()

    while True: 
        print("COMMANDS:\n1 Add a flight\n2 View flights\n3 Update flight info\n4 Assign pilot\n5 View pilot schedule\n6 View destination information\n7 Update destination information\n0 Exit")
        command = input("Please enter the number of the command you would like to use from the above list: \n")
        match command:
            case '1':
                print("command 1")
            case '2':
                print("command 2")
            case '3':
                print("command 3")
            case '4':
                print("command 4")
            case '5':
                print("command 5")
            case '6':
                print("command 6")
            case '7':
                print("command 7")
            case '0':
                break
    cursor.close() # close cursor
    conn.close() # close connection 

    print("Database connection closed.")

# def add_flight():

# def view_flights(): 

# def update_flight_info(): 

# def assign_pilot():

# def view_pilot_schedule(): 

# def view_destination_info():

# def update_destination_info(): 
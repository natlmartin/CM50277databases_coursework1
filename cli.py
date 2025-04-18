## 2.3 Application development in Python 
import cli_addflight
import cli_viewflights
import cli_updateflightinfo
import cli_assignpilot
import cli_pilotschedule
import cli_destinationinfo

# Runs main CLI for application. User supplies a command to call one of the CLI functions. 
def user_interface(conn): 
    while True: 
        print("COMMANDS:\n1 Add a flight\n2 View flights\n3 Update flight info\n4 Assign pilot\n5 View pilot schedule\n6 View/Update destination information\n0 Exit")
        command = input("Please enter the number of the command you would like to use from the above list: \n")
        match command:
            case '1':
                cli_addflight.add_flight(conn)
            case '2':
                cli_viewflights.view_flights(conn)
            case '3':
                cli_updateflightinfo.update_flight_info(conn)
            case '4':
                cli_assignpilot.assign_pilot(conn)
            case '5':
                cli_pilotschedule.view_pilot_schedule(conn)
            case '6':
                cli_destinationinfo.destination_info(conn)
            case '0':
                print("Happy travels!")
                break
            case _:
                print("Input not recognised - please enter a number between 0 - 6.\n")


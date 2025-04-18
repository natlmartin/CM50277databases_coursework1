import sqlite3
import db_schema
import db_queries
import cli

conn = sqlite3.connect('airline.db')

### FUNCTIONS HAVE BEEN COMMENTED OUT FOR TESTING - PLEASE UNCOMMENT TO RUN 

## 2.1 Database setup in SQLite
#db_schema.create_tables(conn)
#db_schema.populate_tables(conn)

## 2.2 SQL queries and database interaction 
# db_queries.flight_retrieval_queries(conn, 'MEX', 'Delayed', '2025-05-08')
# db_queries.schedule_modification(conn, '09:30:00', '2025-05-01', 'On Time', '2025-05-02')
# db_queries.pilot_assignment(conn, 1, 6)
# db_queries.retrieve_destination_information(conn, 'LHR', 1)
# db_queries.summarise_data(conn)

## 2.3 Application development in Python 
#cli.user_interface()

conn.close()
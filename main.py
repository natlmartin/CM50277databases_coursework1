import sqlite3
import db_schema
import db_queries
import cli

conn = sqlite3.connect('airline.db')
print("Connected to database.\n")
cursor = conn.cursor()

## 2.1 Database setup in SQLite
# db_schema.create_tables()
# db_schema.populate_tables()

## 2.2 SQL queries and database interaction 
#db_queries.flight_retrieval_queries()
#db_queries.schedule_modification()
# db_queries.pilot_assignment()
#db_queries.retrieve_destination_information()
#db_queries.summarise_data()

## 2.3 Application development in Python 
cli.user_interface()
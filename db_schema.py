import sqlite3

def create_tables():
    conn = sqlite3.connect('airline.db')
    print("Database created successfully.")
    # enable foreign keys: https://sqlite.org/foreignkeys.html
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()

    # create tables  
    table_creation = """
    CREATE TABLE IF NOT EXISTS flights (
        flight_id INT NOT NULL PRIMARY KEY, departure_airport VARCHAR(20), arrival_airport VARCHAR(20), pilot_id INT, schedule_id INT, plane_id INT, direct_flight BOOLEAN, passenger_capacity INT, ticket_price FLOAT, FOREIGN KEY (departure_airport) REFERENCES destinations (airport_code), FOREIGN KEY (arrival_airport) REFERENCES destinations (airport_code), FOREIGN KEY (pilot_id) REFERENCES pilots (pilot_id), FOREIGN KEY (schedule_id) REFERENCES flight_schedule (schedule_id)
    );     
    CREATE TABLE IF NOT EXISTS flight_schedule (
        schedule_id INT NOT NULL PRIMARY KEY, flight_id INT NOT NULL, departure_date DATE, departure_time TIME, arrival_date DATE, arrival_time TIME, flight_status VARCHAR(20), FOREIGN KEY (flight_id) REFERENCES flights (flight_id)
    );
    CREATE TABLE IF NOT EXISTS pilots (
        pilot_id INT NOT NULL PRIMARY KEY, first_name VARCHAR(20) NOT NULL, last_name VARCHAR(20) NOT NULL, flight_hours INT, rank VARCHAR(20), home_airport VARCHAR(20), FOREIGN KEY (home_airport) REFERENCES destinations (airport_code)
    );
    CREATE TABLE IF NOT EXISTS pilot_contacts (
        pilot_id INT NOT NULL PRIMARY KEY, email VARCHAR(255) NOT NULL, contact_number VARCHAR(20) NOT NULL, addr_first_line VARCHAR(255), addr_second_line VARCHAR(255), addr_city VARCHAR(20), addr_postcode VARCHAR(20), FOREIGN KEY (pilot_id) REFERENCES pilots (pilot_id)
    ); 
    CREATE TABLE IF NOT EXISTS destinations (
        airport_code VARCHAR(20) NOT NULL PRIMARY KEY, city_id VARCHAR(20) NOT NULL, total_runways INT, FOREIGN KEY (city_id) REFERENCES cities (city_id)
    );
    CREATE TABLE IF NOT EXISTS cities (
        city_id VARCHAR(20) NOT NULL PRIMARY KEY, city_name VARCHAR(20), country_code VARCHAR(20)
    );"""
    table_query = """SELECT name FROM sqlite_master WHERE type='table';"""

    cursor.executescript(table_creation)
    cursor.execute(table_query)
    print("The followed tables were created successfully:\n")
    print(cursor.fetchall())

    conn.commit() # save changes
    cursor.close() # close cursor
    conn.close() # close connection 

def populate_tables(): 
    conn = sqlite3.connect('airline.db')
    print("Connected to database successfully.")
    cursor = conn.cursor()

    populate_flights = """INSERT INTO flights (flight_id, departure_airport, arrival_airport, pilot_id, schedule_id, plane_id, direct_flight, passenger_capacity, ticket_price) VALUES 
        (101, 'LHR', 'JFK', 1, 1, 201, TRUE, 250, 799.99),
        (102, 'JFK', 'HND', 2, 2, 202, FALSE, 300, 1200.50),
        (103, 'HND', 'CDG', 3, 3, 203, TRUE, 280, 950.75),
        (104, 'CDG', 'SYD', 4, 4, 204, TRUE, 220, 1050.00),
        (105, 'SYD', 'BER', 5, 5, 205, FALSE, 260, 700.20),
        (106, 'BER', 'DXB', 6, 6, 206, TRUE, 240, 850.40),
        (107, 'DXB', 'YYZ', 7, 7, 207, FALSE, 270, 980.10),
        (108, 'YYZ', 'SVO', 8, 8, 208, TRUE, 230, 720.30),
        (109, 'SVO', 'GIG', 9, 9, 209, FALSE, 290, 870.60),
        (110, 'GIG', 'SIN', 10, 10, 210, TRUE, 310, 1100.80),
        (111, 'SIN', 'MEX', 11, 11, 211, FALSE, 255, 950.90),
        (112, 'MEX', 'CPT', 12, 12, 212, TRUE, 265, 820.00),
        (113, 'CPT', 'HKG', 13, 13, 213, FALSE, 275, 780.20),
        (114, 'HKG', 'FCO', 14, 14, 214, TRUE, 295, 880.40),
        (115, 'FCO', 'LHR', 15, 15, 215, FALSE, 250, 1020.50);
    """
    populate_flight_schedule = """INSERT INTO flight_schedule (schedule_id, flight_id, departure_date, departure_time, arrival_date, arrival_time, flight_status) VALUES 
        (1, 101, '2025-05-01', '08:30:00', '2025-05-01', '12:15:00', 'On Time'),
        (2, 102, '2025-05-02', '10:00:00', '2025-05-02', '14:45:00', 'Delayed'),
        (3, 103, '2025-05-03', '09:15:00', '2025-05-03', '13:00:00', 'On Time'),
        (4, 104, '2025-05-04', '07:45:00', '2025-05-04', '11:30:00', 'Cancelled'),
        (5, 105, '2025-05-05', '12:30:00', '2025-05-05', '16:15:00', 'On Time'),
        (6, 106, '2025-05-06', '06:45:00', '2025-05-06', '10:30:00', 'Delayed'),
        (7, 107, '2025-05-07', '14:15:00', '2025-05-07', '18:00:00', 'On Time'),
        (8, 108, '2025-05-08', '11:30:00', '2025-05-08', '15:15:00', 'On Time'),
        (9, 109, '2025-05-09', '08:00:00', '2025-05-09', '11:45:00', 'On Time'),
        (10, 110, '2025-05-10', '07:15:00', '2025-05-10', '11:00:00', 'Cancelled'),
        (11, 111, '2025-05-11', '13:45:00', '2025-05-11', '17:30:00', 'On Time'),
        (12, 112, '2025-05-12', '06:00:00', '2025-05-12', '09:45:00', 'Delayed'),
        (13, 113, '2025-05-13', '15:30:00', '2025-05-13', '19:15:00', 'On Time'),
        (14, 114, '2025-05-14', '10:45:00', '2025-05-14', '14:30:00', 'On Time'),
        (15, 115, '2025-05-15', '09:00:00', '2025-05-15', '12:45:00', 'On Time');
    """
    populate_pilots = """INSERT INTO pilots (pilot_id, first_name, last_name, flight_hours, rank, home_airport) VALUES 
        (1, 'John', 'Smith', 12000, 'Captain', 'LHR'),
        (2, 'Emily', 'Johnson', 8500, 'First Officer', 'JFK'),
        (3, 'Ken', 'Tanaka', 9500, 'Captain', 'HND'),
        (4, 'Pierre', 'Dubois', 7000, 'First Officer', 'CDG'),
        (5, 'Sarah', 'Williams', 10500, 'Captain', 'SYD'),
        (6, 'Hans', 'Muller', 11000, 'Captain', 'BER'),
        (7, 'Ahmed', 'Al-Farsi', 9800, 'First Officer', 'DXB'),
        (8, 'James', 'Wilson', 9300, 'Captain', 'YYZ'),
        (9, 'Nikolai', 'Petrov', 8200, 'First Officer', 'SVO'),
        (10, 'Carlos', 'Fernandez', 7800, 'First Officer', 'GIG'),
        (11, 'Wei', 'Zhang', 10200, 'Captain', 'SIN'),
        (12, 'Luis', 'Gomez', 8900, 'First Officer', 'MEX'),
        (13, 'Thabo', 'Ngwenya', 7500, 'First Officer', 'CPT'),
        (14, 'David', 'Brown', 9600, 'Captain', 'HKG'),
        (15, 'Antonio', 'Rossi', 8400, 'First Officer', 'FCO');
    """
    populate_pilot_contacts = """INSERT INTO pilot_contacts (pilot_id, email, contact_number, addr_first_line, addr_second_line, addr_city, addr_postcode) VALUES 
        (1, 'john.smith@example.com', '+44 1234 567890', '123 Heathrow St.', NULL, 'London', 'W1A 1AA'),
        (2, 'emily.johnson@example.com', '+1 212 345 6789', '456 JFK Ave.', 'Apartment 2B', 'New York', '10001'),
        (3, 'ken.tanaka@example.com', '+81 90 1234 5678', '789 Haneda Rd.', NULL, 'Tokyo', '100-0001'),
        (4, 'pierre.dubois@example.com', '+33 1 2345 6789', '234 Paris Blvd.', NULL, 'Paris', '75001'),
        (5, 'sarah.williams@example.com', '+61 400 123 456', '567 Sydney Dr.', 'Unit 5', 'Sydney', '2000'),
        (6, 'hans.muller@example.com', '+49 30 1234 5678', '678 Berlin Platz.', NULL, 'Berlin', '10117'),
        (7, 'ahmed.alfarsi@example.com', '+971 50 678 1234', '12 Dubai Tower.', NULL, 'Dubai', '00000'),
        (8, 'james.wilson@example.com', '+1 416 123 4567', '345 Toronto St.', 'Suite 8', 'Toronto', 'M5H 2N2'),
        (9, 'nikolai.petrov@example.com', '+7 495 123 4567', '987 Moscow Rd.', NULL, 'Moscow', '101000'),
        (10, 'carlos.fernandez@example.com', '+55 21 9876 5432', '567 Rio Lane.', NULL, 'Rio de Janeiro', '20000-000'),
        (11, 'wei.zhang@example.com', '+65 9001 2345', '123 Orchard Rd.', NULL, 'Singapore', '238890'),
        (12, 'luis.gomez@example.com', '+52 55 1234 5678', '456 Mexico City Ave.', NULL, 'Mexico City', '01000'),
        (13, 'thabo.ngwenya@example.com', '+27 82 123 4567', '789 Cape Town Blvd.', NULL, 'Cape Town', '8001'),
        (14, 'david.brown@example.com', '+852 9012 3456', '345 Hong Kong Plaza.', NULL, 'Hong Kong', '00000'),
        (15, 'antonio.rossi@example.com', '+39 06 1234 5678', '567 Rome St.', NULL, 'Rome', '00100');
    """
    populate_destinations = """INSERT INTO destinations (airport_code, city_id, total_runways) VALUES
        ('LHR', 'C001', 2),
        ('JFK', 'C002', 4),
        ('HND', 'C003', 3),
        ('CDG', 'C004', 4),
        ('SYD', 'C005', 3),
        ('BER', 'C006', 2),
        ('DXB', 'C007', 3),
        ('YYZ', 'C008', 3),
        ('SVO', 'C009', 2),
        ('GIG', 'C010', 2),
        ('SIN', 'C011', 4),
        ('MEX', 'C012', 3),
        ('CPT', 'C013', 2),
        ('HKG', 'C014', 3),
        ('FCO', 'C015', 2);
    """
    populate_cities = """INSERT INTO cities (city_id, city_name, country_code) VALUES 
        ('C001', 'London', 'UK'),
        ('C002', 'New York', 'US'),
        ('C003', 'Tokyo', 'JP'),
        ('C004', 'Paris', 'FR'),
        ('C005', 'Sydney', 'AU'),
        ('C006', 'Berlin', 'DE'),
        ('C007', 'Dubai', 'AE'),
        ('C008', 'Toronto', 'CA'),
        ('C009', 'Moscow', 'RU'),
        ('C010', 'Rio de Janeiro', 'BR'),
        ('C011', 'Singapore', 'SG'),
        ('C012', 'Mexico City', 'MX'),
        ('C013', 'Cape Town', 'ZA'),
        ('C014', 'Hong Kong', 'HK'),
        ('C015', 'Rome', 'IT');
    """
    cursor.execute(populate_flights)
    print("\nflights records updated successfully")
    cursor.execute(populate_flight_schedule)
    print("\nflight_schedule records updated successfully")
    cursor.execute(populate_pilots)
    print("\npilots records updated successfully")
    cursor.execute(populate_pilot_contacts)
    print("\npilot_contacts records updated successfully")
    cursor.execute(populate_destinations)
    print("\ndestinations records updated successfully")
    cursor.execute(populate_cities)
    print("\ncities records updated successfully\n")
    print("Total number of rows created: ", conn.total_changes)

    conn.commit() # save changes
    cursor.close() # close cursor
    conn.close() # close connection 
def format_sql_output(cursor):
    rows = cursor.fetchall()
    for row in rows:
        print(dict(row), "\n")

def format_tuple_output(cursor):
    rows = cursor.fetchall()
    column_header = [description[0] for description in cursor.description]
    for row in rows:
        print(dict(zip(column_header, row)), "\n")
def format_sql_output(cursor):
    rows = cursor.fetchall()
    for row in rows:
        print(dict(row), "\n")
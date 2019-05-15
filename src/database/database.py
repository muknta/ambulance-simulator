import psycopg2

# conn = psycopg2.connect(host='localhost', port='5432', database='ambulancedb', user='ambulance', password='qwerty')
# cur = conn.cursor()
#
# cur.execute('SELECT * from greeting')
try:
    connection = psycopg2.connect(user="postgres", password="qwerty", port="5432", database="ambulancedb")

    cursor = connection.cursor()
    print(connection.get_dsn_parameters(), "\n")

except (Exception, psycopg2.Error) as error :
    print("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection.
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")

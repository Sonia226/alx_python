"""
This module lists all cities of the state from the database
"""
import MySQLdb
import sys

if __name__ == '__main__':

    # checks if length of arguments is not equal to 5
    if len(sys.argv) != 5:
        print('Pls use: {} <mysql_username> <mysql_password>'
              '<database_name> <state_name>'.format(sys.argv[0]))

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
    try:

        # Connect to the MySQL server
        database = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )

# Create a cursor object
        cursor = database.cursor()

# Execute the SQL query
        query = """SELECT cities.name
        FROM cities JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id"""

        cursor.execute(query, (state_name,))

# Fetch all the rows
        cities = cursor.fetchall()

# Display the results
        city_names = [row[0] for row in cities]
        print(", ".join(city_names))

# Close the cursor and database connection
        cursor.close()
        database.close()

    except MySQLdb.Error as e:
        print('MySQL Error:', e)
        sys.exit(1)
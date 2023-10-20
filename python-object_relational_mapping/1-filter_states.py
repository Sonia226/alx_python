"""
This is module filters states starting with N from the database
"""
import MySQLdb
import sys

if __name__ == '__main__':

    # checks if length of arguments is not equal to 4
    if len(sys.argv) != 4:
        print('Pls use: 0-select_states.py'
              ' <mysql_username> <mysql_password> <database_name>')

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

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
        cursor.execute(
            "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id")

# Fetch all the rows
        states = cursor.fetchall()

# Display the results
        for state in states:
            print(state)

# Close the cursor and database connection
        cursor.close()
        database.close()

    except MySQLdb.Error as e:
        print('MySQL Error:', e)
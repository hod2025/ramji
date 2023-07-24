import mysql.connector

# Establish a database connection
try:
    # Replace the following placeholders with your database credentials
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='manager',
        database='lalit'
    )
    print("Connected to the database.")
except mysql.connector.Error as err:
    print("Error connecting to the database:", err)
    exit()

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Create a table (if it doesn't exist)
create_table_query = """
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    department VARCHAR(100)
)
"""

try:
    cursor.execute(create_table_query)
    print("Table 'employees' created successfully.")
except mysql.connector.Error as err:
    print("Error creating table:", err)
    exit()

# Insert records into the table
insert_records_query = """
INSERT INTO employees (name, age, department)
VALUES (%s, %s, %s)
"""

# Sample records to insert into the table
records_to_insert = [
    ('khumesh', 30, 'IT'),
    ('pradip', 25, 'HR'),
    ('jayesh', 35, 'Finance')
]

try:
    cursor.executemany(insert_records_query, records_to_insert)
    connection.commit()
    print("Records inserted successfully.")
except mysql.connector.Error as err:
    print("Error inserting records:", err)
    connection.rollback()

# Display table records
select_query = "SELECT * FROM employees"

try:
    cursor.execute(select_query)
    records = cursor.fetchall()
    print("\nDisplaying table records:")
    for record in records:
        print(record)
except mysql.connector.Error as err:
    print("Error fetching records:", err)

# Close the cursor and database connection
cursor.close()
connection.close()

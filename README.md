* SQLite3 Database Management Class in Python
Welcome to the SQLite3 Database Management Class project! This repository provides a comprehensive and user-friendly object-oriented Python class designed to simplify interactions with SQLite3 databases. Whether you are a beginner or an experienced developer, this class offers a robust solution for managing your data seamlessly.

Features
✨ Key Features of the Database Class:

Create Tables: Effortlessly define new tables with customizable column specifications to suit your data needs.

Insert Data: Quickly insert multiple records into your tables in a single operation, enhancing data entry efficiency.

Fetch Data: Retrieve data from tables with optional filtering conditions, enabling precise queries and streamlined data access.

Update Data: Modify existing records with ease, ensuring data integrity by specifying conditions for updates.

Delete Data: Remove specific records from tables, providing the flexibility to manage your database effectively.

Export to Excel: Utilize the power of the pandas library to export table data to Excel files, facilitating easy data sharing and analysis.

Check Data Existence: Verify the presence of specific data in your database to enhance your data validation processes.

Installation
To use the Database class, you'll need to have Python installed on your system along with the pandas library. You can install pandas using pip:

bash
pip install pandas
Once you have the prerequisites, you can clone this repository:

bash
git clone https://github.com/yourusername/your-repository-name.git
Usage
Here’s a quick guide to get you started with the Database class:

python:
import pandas as pd
import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()

    def create_table(self, table_name, *columns):
        # Create a new table
        ...

    def insert_data(self, table_name, *values):
        # Insert data into a table
        ...

    def fetch_data(self, table_name, condition=None):
        # Fetch data from a table
        ...

    def update_data(self, table_name, set_condition, condition):
        # Update existing data in a table
        ...

    def delete_data(self, table_name, condition):
        # Delete data from a table
        ...

    def export_to_excel(self, table_name, file_name):
        # Export table data to an Excel file
        ...

    def exists(self, table_name, condition):
        # Check if specific data exists in a table
        ...
Example
Here’s a simple example demonstrating the use of the Database class:

python
Kodu kopyala
# Create a new database instance
db = Database('test.sqlite3')

# Create a new table
db.create_table('users', 'name TEXT', 'surname TEXT', 'birth_year INTEGER')

# Insert data into the table
db.insert_data("users", "John", "Doe", 1990)

# Fetch and print data from the table
print(db.fetch_data("users"))

# Update data in the table
db.update_data("users", "name='Jane'", "rowid=1")

# Check if data exists
if db.exists("users", "name='Jane'"):
    print("Data exists!")

# Export data to an Excel file
db.export_to_excel("users", "users_data")
Contribution
Contributions are welcome! If you have suggestions for improvements or features, feel free to create an issue or submit a pull request. Together, we can make this project even better!

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any inquiries or further information, please contact:

Your Name: jinonen@gmail.com
GitHub: BilgeJINONEN


import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

def connect_db():
    connection = psycopg.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

    return connection


def get_employees():
    db = connect_db() #just to establish connection to the database

    try:
        cursor = db.cursor() #.cursor() used to create an object that allows SQL commands inside the function

        cursor.execute("SELECT * FROM employees") #hightlight data and copy it to the clipboard

        records = cursor.fetchall() #paste the copied data into the code

        return records #pass the data back to the records variable

    finally:
        db.close() #.close() closes the connection to the database


if __name__ == "__main__":
    try:
        employees = get_employees() #run the function of the get_employees() to get the data from the stored value earlier

        for employee in employees: #get
            print(employee) 

    except psycopg.Error as error:
        print("Database error:", error)

def insert_employee(name, department, salary): 
    db = connect_db() #establish connection to the database

    try:
        cursor = db.cursor() #allows SQL commands to be executed in the database
        cursor.execute(
            "INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)",
            (name, department, salary)
        ) #execute the SQL command
        db.commit()  # Commit the transaction to save changes
        print("Employee added successfully.") #prints after the transaction completes

    except psycopg.Error as error:
        print("Database error:", error)

    finally:
        db.close() #closes the database connection

def find_employee(name):
    db = connect_db()  # Establish connection to the database

    try:
        cursor = db.cursor()  # Allows SQL commands to be executed in the database
        cursor.execute(
            "SELECT * FROM employees WHERE name ILIKE %s",
            (f"%{name}%",)
        )  # Execute the SQL command with case-insensitive search
        records = cursor.fetchall()  # Fetch all matching records

        return records  # Return the matching records

    except psycopg.Error as error:
        print("Database error:", error)

    finally:
        db.close()  # Close the database connection

def del_employee(employee_id):
    db = connect_db()

    try:
        cursor = db.cursor()

        cursor.execute(
            "DELETE FROM employees WHERE employee_id = %s",
            (employee_id,)
        )

        deleted_count = cursor.rowcount
        db.commit()

        if deleted_count > 0:
            print("Employee deleted successfully.")
        else:
            print("Employee not found.")

    except psycopg.Error as error:
        db.rollback()
        print("Database error:", error)

    finally:
        db.close()

def employee_exists(name):
    db = connect_db()

    try:
        cursor = db.cursor()

        cursor.execute(
            "SELECT EXISTS(SELECT 1 FROM employees WHERE LOWER(name) = LOWER(%s))",
            (name,)
        )

        return cursor.fetchone()[0]

    finally:
        db.close() 

def change_employee(employee_id, name=None, department=None, salary=None):
    db = connect_db()

    try:
        cursor = db.cursor()

        # Build the update query dynamically based on provided parameters
        update_fields = []
        update_values = []

        if name is not None:
            update_fields.append("name = %s")
            update_values.append(name)
        if department is not None:
            update_fields.append("department = %s")
            update_values.append(department)
        if salary is not None:
            update_fields.append("salary = %s")
            update_values.append(salary)

        if not update_fields:
            print("No fields to update.")
            return

        update_query = f"UPDATE employees SET {', '.join(update_fields)} WHERE employee_id = %s"
        update_values.append(employee_id)

        cursor.execute(update_query, tuple(update_values))
        db.commit()

        if cursor.rowcount > 0:
            print("Employee updated successfully.")
        else:
            print("Employee not found.")

    except psycopg.Error as error:
        db.rollback()
        print("Database error:", error)

    finally:
        db.close()


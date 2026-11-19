from database import insert_employee, get_employees, find_employee, del_employee, change_employee, employee_exists

def add_employee():
    name = input("Please provide your name: ").strip()

    if employee_exists(name):
        print("Employee with this name already exists.")
        return

    salary = validate_salary()

    department = input("Please provide your department: ")

    insert_employee(name, department, salary)

def display_employees(records):
    print(f"{'ID':<5}{'Name':<20}{'Salary':>15}  {'Department'}")
    print("-" * 65)

    for employee in records:
        print(f"{employee[0]:<5}{employee[1]:<20}{employee[2]:>15,.2f}{employee[3]}") 

def validate_salary():
    while True:
        try:
            salary = float(input("Please provide your salary: "))

            if salary <= 0:
                print("Invalid salary. Please enter a positive amount.")
            else:
                return salary

        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        
    
def view_employee(): 
    employees = get_employees()

    if not employees: 
        print("No employees found")
    else: 
        for employee in employees:
            print(employee)
            
def search_employee():
    search_name = input("Enter employee name: ") 

    records = find_employee(search_name)

    if records is None:
        return

    if not records:
        print("Employee not found.")
    else:
        for employee in records:
            print(employee)


def update_employee():
    view_employee()

    try:
        employee_id = int(input("Enter employee ID to update: "))

        new_salary = validate_salary()

        new_department = input("Enter new department: ")

        change_employee(
            employee_id,
            department=new_department,
            salary=new_salary
        )

    except ValueError:
        print("Invalid employee ID.")

def delete_employee():
    view_employee()

    try:
        employee_id = int(input("Enter employee ID to delete: "))

        confirmation = input("Are you sure? (yes/no): ")

        if confirmation.lower() == "yes":
            del_employee(employee_id)
        else:
            print("Deletion cancelled.")

    except ValueError:
        print("Invalid employee ID.")


while True: 
    print("1. Add Employee")
    print("2. View Employee")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1": 
        add_employee()
        
    elif choice == "2": 
        view_employee()
        
    elif choice == "3": 
        search_employee()
        
    elif choice == "4":
        update_employee()

    elif choice == "5":
        delete_employee()

    elif choice == "6":
        print("Exiting..")
        break
    else: 
        print("invalid choice")
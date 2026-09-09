import json
import csv

employees = [ 
    {

    "id": 1,
    "name": "Ravi Kumar", 
    "department": "Sales", 
    "basic_salary": 30000, 
    "allowances": 5000, 
    "deductions": 2000

     }, 
     {

    "id": 2, 
    "name": "Anita Rao", 
    "department": "IT", 
    "basic_salary": 45000, 
    "allowances": 8000, 
    "deductions": 3000

    } 
] 


next_id = len(employees) + 1

def add_employee():

    global next_id

    while True:
        ename = input("Enter the employee name : ")

        if ename == "":
            print("name cannot be emptied, please try again!")

        else:
            break

    while True:
        department = input("Enter the department name : ")
        
        if department == "":
                print("department cannot be emptied, please try again!")
        
        else:
            break 

    while True:

        try:
            basic_salary = float(input("Enter the basic salary: "))

            if basic_salary <= 0:
                print("Basic salary should be greater than 0, please try again")

            else:
                break

        except ValueError:
            print("Enter valid choice!")
        

    while True:

        try:
            allowances = float(input("Enter the basic salary: "))

            if allowances <= 0:
                print("Allowances should be greater than 0, please try again")

            else:
                break

        except ValueError:
            print("Enter valid choice!")


    while True:
        deductions = float(input("Enter the basic salary: "))

        f_salary = allowances + basic_salary

        if deductions <= 0:
            print("Deductions should be greater than 0, please try again")

        elif f_salary <= deductions:
            print("Deductions cannot be exceeded!, please try again!")

        else:
            break

    net_salary = basic_salary + allowances - deductions

    employee = {
        "id": next_id,
        "name": ename,
        "department": department,
        "basic_salary": basic_salary,
        "allowances": allowances,
        "deductions": deductions
    }


    employees.append(employee)
    print(employee)
    print("Employee Added Successfully!")

    next_id += 1

def view_all_employees():

    if len(employees) == 0:
        print("Enter employee not found!")
        return

    print("\nView all Employees: ")

    print("="*95)

    print(
        f"{"ID":<5}"
        f"{"Name":<5}"
        f"{"Department":<5}"
        f"{"Basic_salary":<5}"
        f"{"Allowances":<5}"
        f"{"Deductions":<5}"
    )    

    print("-"*95)

for employee in employees:

    print(
        f"{employee['id']:<5}"
        f"{employee['name']:<5}"
        f"{employee['department']:<5}"
        f"{employee['basic_salary']:<5}"
        f"{employee['allowances']:<5}"
        f"{employee['deduction']:<5}"
        
    )

    print("="*95)


def main():

     while True:
    
            print("\n===== PRODUCT INVENTORY MANAGEMENT SYSTEM =====")
            print("1. Add Employee")
            print("2. View All Employee")
            print("3. Search Employee")
            print("4. Update Employee")
            print("5. Delete Employee")
            print("6. Exit")
    
            choice = input("Enter your choice: ")
    
            if choice == "1":
                add_employee()
    
            elif choice == "2":
                view_products()
    
            elif choice == "3":
                search_product()
    
            elif choice == "4":
                update_product()
    
            elif choice == "5":
                delete_product()
    
            elif choice == "6":
                print("Thank you for using the Inventory Management System!")
                break
    
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()  
'''
Create a small program that contains a list of employee names.
Print out the list of names when the program runs the first time.
Prompt for an employee name and remove that specific name from the list of names.
Display the remaining employees, each on its own line.

Example Output
There are 5 employees:
John Smith
Jackie Jackson
Chris Jones
Amanda Cullen
Jeremy Goodwin

Enter an employee name to remove: Chris Jones
There are 4 employees:
John Smith
Jackie Jackson
Amanda Cullen
Jeremy Goodwin
'''

def employee_shorting(emp_name):

    print(f"There are {len(emp_name)} employees:")
    for name in emp_name:
        print(name)
    print()

    rem_emp_name = input("Type the employee name to remove: ")

    #safely remove the employee
    if rem_emp_name in emp_name:
        emp_name.remove(rem_emp_name)
        print(f"There are {len(emp_name)} employees now: ")
        for name in emp_name:
            print(name)
        # print(emp_name)
    else:
        print(f"Employee: {rem_emp_name} not found.")

    

emp_name = ["Manoj", "Sivaji", "Amit", "Varsha", "Pinky"]
employee_shorting(emp_name)



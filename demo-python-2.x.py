# A sample Python 2.x script for generating a report

import sys
import os

def get_employees(filename):
    """
    Reads employee names from a file.
    Note: In Python 2, input is used to get strings.
    """
    if not os.path.exists(filename):
        # Python 2 syntax for raising exceptions
        raise IOError, "File not found: " + filename

    employees = []
    with open(filename, 'r') as f:
        for line in f:
            # Python 2 handles file lines as byte strings by default
            employees.append(line.strip())
    return employees

def generate_report(employees):
    """
    Generates a simple report of employee data.
    """
    # Print is a statement in Python 2, not a function
    print("--- Employee Report ---")
    print "Total employees:", len(employees)
    print("First employee:", employees[0])

    # Integer division behavior is different in Python 2
    print "Average employee ID per file (using integer division):", 10 / 3

    # The range iterator is used for performance in Python 2
    for i in range(len(employees)):
        print "Processing employee #%d" % (i + 1)

def main():
    # input is used for string input in Python 2
    filepath = input("Enter the path to the employee list file: ")
    try:
        employee_list = get_employees(filepath)
        generate_report(employee_list)
    # Python 2 syntax for catching exceptions
    except IOError, e:
        # String formatting using the old % operator
        print("ERROR: %s" % e)
    except Exception, e:
        print("An unexpected error occurred:", e)

if __name__ == '__main__':
    main()


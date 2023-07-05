#!/usr/bin/python3
"""Displays tasks information of a given employee
"""
import requests
import sys


def get_data(url):
    """Utility method to get data from any api endpoint and parse the json
    params:
        - url (str) - the URL endpoint
    """
    request = requests.get(url)

    if request.status_code == 200:
        try:
            return request.json()
        except:
            raise Exception("")


def main():
    """The main function from which the whole program starts
    """
    # Extract the user id from the script arguments
    employee_id = sys.argv[1]

    # Getting the name
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    name = get_data(user_url)["name"]

    # Getting the todos
    tasks_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    todos = get_data(tasks_url)

    total_number_of_todos = len(todos)
    number_of_completed_todos = 0

    for todo in todos:
        if todo["completed"]:
            number_of_completed_todos += 1
    

    print(f'Employee {name} is done with tasks({number_of_completed_todos}/{total_number_of_todos})')

    for todo in todos:
        if todo["completed"]:
            print(f'\t {todo["title"]}')



if __name__ == "__main__":
    main()

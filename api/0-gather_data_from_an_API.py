#!/usr/bin/python3
"""Displays tasks information of a given employee
Trying two lines
"""
from requests import get
from sys import argv


def get_data(url):
    """Utility method to get data from any api endpoint and parse the json
    params:
        - url (str) - the URL endpoint
    """
    request = get(url, verify=False)

    if request.status_code == 200:
        try:
            return request.json()
        except:
            raise Exception("")
    else:
        raise Exception(request.status_code)


def main():
    """The main function from which the whole program starts
    """

    # Base url
    base_url = 'https://jsonplaceholder.typicode.com'

    # Extract the user id from the script arguments
    employee_id = argv[1]

    # Getting the name
    user_url = base_url + "/users/" + employee_id
    name = get_data(user_url).get('name')

    # Getting the todos
    tasks_url = base_url + '/todos?userId=' + employee_id
    todos = get_data(tasks_url)

    n_todos = len(todos)
    n_completed_todos = 0

    for todo in todos:
        if todo.get('completed'):
            n_completed_todos += 1

    print(
        'Employee ' + name + ' is done with tasks(' + str(n_completed_todos) + '/' + str(n_todos) + '):')

    for todo in todos:
        if todo.get('completed'):
            print('\t ' + todo.get("title"))


if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""
Exports user task data to a csv file
"""
from requests import get
from json import dump


def get_data(url):
    """gets data from an api"""
    request = get(url, verify=False)

    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(request.status_code)


def main():
    """program starting point"""

    # Get users
    users_data_url = 'https://jsonplaceholder.typicode.com/users'
    users = get_data(users_data_url)

    # Create a user hashmap for faster lookup
    users_hashmap = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        users_hashmap[user_id] = username

    # Get todos
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    todos = get_data(todos_url)

    # Data object to write
    data = {}

    # Add todos to data object
    for todo in todos:
        user_id = todo["userId"]
        task_data = { 
            'username': users_hashmap.get(user_id),
            'task': todo.get('title'),
            'completed': todo.get('completed')
        }

        if user_id not in data:
            data[user_id] = []

        user_todos = data[user_id]
        user_todos.append(task_data)
        data[user_id] = user_todos

    with open(f'todo_all_employees.json', 'w') as f:
        dump(data, f)


if __name__ == "__main__":
    main()

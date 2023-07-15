#!/usr/bin/python3
"""
Exports user task data to a csv file
"""
from requests import get
from json import dump
from sys import argv


def get_data(url):
    """gets data from an api"""
    request = get(url, verify=False)

    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(request.status_code)


def main():
    """program starting point"""
    user_id = argv[1]
    base_url = 'https://jsonplaceholder.typicode.com'

    # Get user data
    user_data_url = base_url + '/users/{}'.format(user_id)
    username = get_data(user_data_url).get('username')

    # Get todos
    todos_url = base_url + '/todos?userId={}'.format(user_id)
    todos = get_data(todos_url)

    # Data object to write
    data = {}
    todos_to_write = []

    for todo in todos:
        todo_to_write = {
            'username': username,
            'task': todo.get('title'),
            'completed': todo.get('completed')
        }
        todos_to_write.append(todo_to_write)

    data[user_id] = todos_to_write

    with open(f'{user_id}.json', 'w') as f:
        dump(data, f)


if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""
Exports user task data to a csv file
"""
from requests import get
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
    user_data_url = '{}/users/{}'.format(base_url, user_id)
    username = get_data(user_data_url).get('username')

    # Get todos
    todos_url = '{}/todos?userId={}'.format(base_url, user_id)
    todos = get_data(todos_url)

    # Create text to write
    text = ''

    for todo in todos:
        todo_status = todo.get('completed')
        todo_title = todo.get('title')
        text += '"{}","{}","{}","{}"\n'.format(
                user_id, username, todo_status, todo_title)

    with open('{}.csv'.format(user_id), "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()

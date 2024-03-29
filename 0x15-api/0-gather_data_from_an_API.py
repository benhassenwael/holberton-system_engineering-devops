#!/usr/bin/python3
"""Script to get information from the TODO api endpoint as it
pertains to a particular employee identified by ID."""
import requests
import sys


user_api = 'https://jsonplaceholder.typicode.com/users/'


def get_user_todos(user_id):
    """Get TODO list for a user id """
    try:
        todos = requests.get(user_api + user_id + '/todos')
        todos.raise_for_status()
        return todos.json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


def get_user_name(user_id):
    """Get user name identified by user_id"""
    try:
        user = requests.get(user_api + user_id)
        user.raise_for_status()
        return user.json().get('name')
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        exit(1)

    user_id = sys.argv[1]
    todos = get_user_todos(user_id)
    completed = list(filter(lambda t: t.get('completed') is True, todos))
    name = get_user_name(user_id)

    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          len(completed),
                                                          len(todos)))
    for task in completed:
        print("\t {}".format(task.get('title')))

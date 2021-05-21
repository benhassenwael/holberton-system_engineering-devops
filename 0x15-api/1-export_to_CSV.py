#!/usr/bin/python3
"""Script to get information from the TODO api endpoint as it
pertains to a particular employee identified by ID."""
import csv
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
        return user.json().get('username')
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        exit(1)

    user_id = sys.argv[1]
    todos = get_user_todos(user_id)
    name = get_user_name(user_id)

    data = [dict(userId=user_id,
                 username=name,
                 completed=task.get('completed'),
                 title=task.get('title'))
            for task in todos]
    with open('{}.csv'.format(user_id), 'w', newline="") as f:
        fieldnames = ["userId", "username", "completed", "title"]
        writer = csv.DictWriter(f, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        writer.writerows(data)

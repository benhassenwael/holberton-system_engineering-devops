#!/usr/bin/python3
"""Script to get information from the TODO api endpoint as it
pertains to a particular employee identified by ID."""
import json
import requests


user_api = 'https://jsonplaceholder.typicode.com/users'
todo_api = 'https://jsonplaceholder.typicode.com/todos'


def get_all_todos():
    """Get TODO list for a all users"""
    try:
        todos = requests.get(todo_api)
        todos.raise_for_status()
        return todos.json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


def get_all_users():
    """Get all users"""
    try:
        user = requests.get(user_api)
        user.raise_for_status()
        return user.json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

if __name__ == "__main__":
    todos = get_all_todos()
    users = get_all_users()
    data = {
        u['id']: [dict(task=todo.get('title'),
                       completed=todo.get('completed'),
                       username=u.get('username'))
                  for todo in filter(
                          lambda t: t.get('userId') == u.get('id'), todos
                  )] for u in users
    }
    with open("todo_all_employees.json", 'w') as f:
        json.dump(data, f)

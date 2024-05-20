#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress
"""
import json
import requests
import sys

if __name__ == "__main__":
    u_id = sys.argv[1]
    link_user = f"https://jsonplaceholder.typicode.com/users/{u_id}"
    link_todo = f"https://jsonplaceholder.typicode.com/todos?userId={u_id}"
    res_user = requests.get(link_user)
    res_todo = requests.get(link_todo)
    user_name = res_user.json()['name']
    user_todo = res_todo.json()

    tasks = 0

    for task in user_todo:
        if task['completed']:
            tasks += 1

    print(f"Employee {user_name} is done with tasks \
          ({tasks}/{len(user_todo)}): ")

    for task in user_todo:
        if task['completed']:
            print("\t " + task['title'])

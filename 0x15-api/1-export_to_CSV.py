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
    user_name = res_user.json()['username']
    user_todo = res_todo.json()
    nl = '\n'
    with open(f"{u_id}.csv", 'w', encoding='UTF8') as f:
        for task in user_todo:
            f.write(f""""{u_id}","{user_name}","{task['completed']}",\
"{task['title']}"{nl}""")

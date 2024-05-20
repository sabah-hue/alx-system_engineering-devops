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
    link_user = f"https://jsonplaceholder.typicode.com/users"
    link_todo = f"https://jsonplaceholder.typicode.com/todos"
    res_user = requests.get(link_user)
    res_todo = requests.get(link_todo)
    user_data = res_user.json()
    todo_data = res_todo.json()
    my_arr = []
    for u in user_data:
        for t in todo_data:
            if u['id'] == t['userId']:
                r = {"username": u['username'], "task": t['title'],
                     "completed": t['completed']}
                my_arr.append(r)
                x = u['id']
        print(my_arr)
        data = {x: my_arr}
        with open("todo_all_employees.json", 'w', encoding='UTF8') as f:
            json.dump(data, f)

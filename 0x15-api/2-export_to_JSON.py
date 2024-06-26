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
    u_n = res_user.json()['username']
    user_todo = res_todo.json()
    my_arr = []
    for t in user_todo:
        r = {"task": t['title'], "completed": t['completed'], "username": u_n}
        my_arr.append(r)
    print(my_arr)
    data = {u_id: my_arr}
    with open(f"{u_id}.json", 'w', encoding='UTF8') as f:
        json.dump(data, f)

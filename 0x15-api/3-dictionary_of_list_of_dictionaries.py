#!/usr/bin/python3
"""
    Module contains script that use REST API for a given employee ID,
    returns information about his/her TODO list progress and export
    the data in the JSON format
"""
import json
import requests

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    res = requests.get(url + "users/")
    task_dict = {}
    for employee in res.json():
        username = employee.get('username')
        id = employee.get('id')
        
        todo_res = requests.get(url + "todos")
        all_task = []
        for todo in todo_res.json():
            task = {}
            if todo.get('userId') == id:
                task['username'] = username
                task['task'] = todo.get('title')
                task['complete'] = todo.get('completed')
                all_task.append(task)
        task_dict[id] = all_task
    filename = "todo_all_employees.json"
    with open(filename, mode='w', encoding='utf-8') as a_file:
        json.dump(task_dict, a_file)

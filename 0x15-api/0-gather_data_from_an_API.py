#!/usr/bin/python3
"""Module contains script that use REST API for a given employee ID,
    returns information about his/her TODO list progress
"""
import requests
import sys

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    res = requests.get(url + "users/{}".format(sys.argv[1]))
    employee_name = res.json().get('name')
    res = requests.get(url + "todos")
    total_task = 0
    completed_task = 0
    task_title = ""
    for todo in res.json():
        if todo.get('userId') == int(sys.argv[1]):
            total_task += 1
            if todo.get('completed'):
                completed_task += 1
                task_title += "\n\t "
                task_title += todo.get('title')
    print("Employee {} is done with tasks ({}/{}):".format(
          employee_name, completed_task, total_task), end="")
    print(task_title)

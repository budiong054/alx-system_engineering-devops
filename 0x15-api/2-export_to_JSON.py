#!/usr/bin/python3
"""
    Module contains script that use REST API for a given employee ID,
    returns information about his/her TODO list progress and export
    the data in the JSON format
"""
import json
import requests
import sys

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]
    res = requests.get(url + "users/{}".format(userId))
    username = res.json().get('username')
    res = requests.get(url + "todos")
    all_task = []
    for todo in res.json():
        task = {}
        if todo.get('userId') == int(userId):
            task['task'] = todo.get('title')
            task['completed'] = todo.get('completed')
            task['username'] = username
            all_task.append(task)
    task_dict = {userId: all_task}
    filename = "{}.json".format(userId)
    with open(filename, mode='w', encoding='utf-8') as a_file:
        json.dump(task_dict, a_file)

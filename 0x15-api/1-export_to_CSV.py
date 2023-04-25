#!/usr/bin/python3
"""
    Module contains script that use REST API for a given employee ID,
    returns information about his/her TODO list progress and export
    the data in the CSV format
"""
import requests
import sys

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]
    res = requests.get(url + "users/{}".format(userId))
    username = res.json().get('username')
    res = requests.get(url + "todos")
    all_task = ''
    for todo in res.json():
        if todo.get('userId') == int(userId):
            line = '"{}","{}","{}","{}"\n'.format(
                    todo.get('userId'),
                    username,
                    todo.get('completed'),
                    todo.get('title')
                )
            all_task += line
    filename = "{}.csv".format(userId)
    with open(filename, mode='w', encoding='utf-8') as a_file:
        a_file.write(all_task)

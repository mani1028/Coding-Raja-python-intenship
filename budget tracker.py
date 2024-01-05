import os
from tabulate import tabulate

tasks = []

def add_task(name, priority, due_date):
    task = {'name': name, 'priority': priority, 'due date': due_date}
    tasks.append(task)

def display_tasks():
    headers = ['Name', 'Priority', 'Due Date']
    data = [[task['name'], task['priority'], task['due date']] for task in tasks]
    print(tabulate(data, headers, tablefmt='pretty'))

def save_tasks():
    with open('tasks.txt', 'w') as f:
        for task in tasks:
            f.write(f"{task['name']},{task['priority']},{task['due date']}\n")

def load_tasks():
    if os.path.exists('tasks.txt'):
        with open('tasks.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                name, priority, due_date = line.strip().split(',')
                add_task(name, priority, due_date)

def delete_task(name):
    global tasks
    tasks = [task for task in tasks if task['name'] != name]

def edit_task(name, priority, due_date):
    global tasks
    tasks = [task if task['name'] != name else {'name': name, 'priority': priority, 'due date': due_date} for task in tasks]

add_task('Finish personal budget tracker', 'high', '2022-12-31')
add_task('Write a blog post about Python programming', 'medium', '2022-12-01')
add_task('Send personal budget tracker to a friend', 'low', '2022-12-15')

display_tasks()
save_tasks()
load_tasks()
delete_task('Send personal budget tracker to a friend')
edit_task('Write a blog post about Python programming', 'high', '2022-12-10')
display_tasks()

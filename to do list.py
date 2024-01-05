import os
from tabulate import tabulate

tasks = []

def add_task(name, priority, due_date):
    task = {'name': name, 'priority': priority, 'due_date': due_date}
    tasks.append(task)

def display_tasks():
    print("\n")
    headers = ['Name', 'Priority', 'Due Date']
    table = [[task[header] for header in headers] for task in tasks]
    print(tabulate(table, headers, tablefmt='grid'))

def update_task(name, new_priority, new_due_date):
    for task in tasks:
        if task['name'] == name:
            task['priority'] = new_priority
            task['due_date'] = new_due_date
            break

def delete_task(name):
    global tasks
    tasks = [task for task in tasks if task['name'] != name]

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nWelcome to To-Do List App\n")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter task name: ")
            priority = input("Enter task priority (Low, Medium, High): ")
            due_date = input("Enter due date (MM/DD/YYYY): ")
            add_task(name, priority, due_date)
        elif choice == '2':
            display_tasks()
        elif choice == '3':
            name = input("Enter task name: ")
            new_priority = input("Enter new task priority (Low, Medium, High): ")
            new_due_date = input("Enter new due date (MM/DD/YYYY): ")
            update_task(name, new_priority, new_due_date)
        elif choice == '4':
            name = input("Enter task name: ")
            delete_task(name)
        elif choice == '5':
            print("Exiting the app...")
            break
        else:
            print("Invalid choice. Please enter a valid choice.")

if __name__ == "__main__":
    main()

import datetime
import logging
# task_list = ["Pradėti sportuoti", "Gerti daug vandens"]

from datetime import date

def add_task():
    while True:
        datetime.date = "YYYY-MM-DD"
        task = input("what is your task?:")
        input(f"Enter due date the task must be completed\n{datetime.date}:")
        tasks_list = []
        # if date in task:
        #     print("date is valid")
        #     break
        # elif date  < 1894:
        #     print("This date is not volid")
        # else:
        #     "It doesnt seem valid"

        # for task in task_list:
        #     running = False
        #     for date in date_list:
        #         print(task)
        #         print(date)
        #         print(date in task)
        #         if task in date:
        #             running = True
        #             break
        #     if not running:
        #             return False
        # return True
        # print("Task well done")
    # else:
    #     if

def display_tasks(tasks_list, add_task()):
    task_list = []

    print(task_list[0])
    print(task_list[1])
    print(task_list[2])
    print(task_list[3])
def main():
   while True:
       print("\nTo-Do List Options:")
       print("1. Add task")
       print("2. Display tasks")
       print("3. Mark task as completed (BONUS)")
       print("4. Delete task")
       print("5. Search task (BONUS)")
       print("6. Edit task (BONUS)")
       print("7. QUIT")
       option = int(input('Enter your choice:'))
       if option == 1:
           add_task()
       elif option == 2:
           display_tasks()
       elif option == 3:
           mark_task_completed()
       elif option == 4:
           delete_task()
       elif option == 5:
           search_tasks()
       elif option == 6:
           edit_task()
       elif option == 7:
           print('Exiting task list!')
           exit()
       else:
           print('Invalid option. Please enter a number between 1 and 6.')

main()
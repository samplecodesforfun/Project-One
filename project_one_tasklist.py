import tkinter as tk

window = tk.Tk()
window.mainloop()


#list that stores all our currently saved tasks
task_list = []

#method to run the task program on the terminal
def interface():
    loadTaskList()
    while(True):
        print("Would you like to view your tasks, add a new task, or remove an old task?")
        print("Enter exit if your finished.")
        user_input = input()
        if(user_input == "view"):
            viewTaskList()
        elif(user_input == "add"):
            addTask()
        elif(user_input == "remove"):
            subtractTask()
        elif(user_input == "exit"):
            break
        else:
            print("user input error")

#loads our task list from the previous save on our text file
def loadTaskList():
    task_file = open("tasklist.txt", "r")
    tasks = task_file.readlines()
    task_file.close()
    for task in tasks:
        if task[-1] == "\n":
            task_list.append(task[:-1])
        else:
            task_list.append(task)


#method to view the current list
def viewTaskList():
    for task in task_list:
        #takes the index of the task in the list and adds 1 to show its task # and task name and prints it
        print(int(task_list.index(task)+1), task)

#method to add new tasks to the list
def addTask():
    task_name = input("What task would you like to add:")
    task_number = int(input("What task # would you like to assign this task: "))
    # makes sure the step number entered cannont be 0 or less than 0
    while task_number <= 0:
        print("The task number cannot be 0 or a negative number.");
        task_number = int(input("What task # would you like to assign this task: "))
    task_list.insert(task_number-1,task_name)

    #adds our new task to the save file, empties the list, and re adds all the tasks in order to the save file
    task_file = open("tasklist.txt", "w")
    task_file.write('');
    for task in task_list:
        task_file.write(task + "\n")
    task_file.close()

    
#method to remove old tasks that were completed
def subtractTask():
    old_task = input("What task would you like to remove: ")
    task_list.remove(old_task)
    
    # removes our old task from the save file, empties the list, and re adds all the remaining tasks in order
    task_file = open("tasklist.txt", "w")
    task_file.write('');
    for task in task_list:
        task_file.write(task + "\n")
    task_file.close()


#loadTaskList()
#viewTaskList()
#addTask()
#subtractTask()
#interface()
#list that stores all our currently saved tasks
task_list = []

#method to run the task program on the terminal
def interface():
    user_input = input("Would you like to view your tasks, add a new task, or remove an old task?")
    if(user_input == "view"):
        print("hi")
    elif(user_input == "add"):
        print("hello")
    elif(user_input == "remove"):
        print("bonjour")
    else:
        print("error")

#method to view the current list
def viewTaskList():
    print(task_list)

# method to add new tasks to the list
def addTask():
    new_task = input("What task would you like to add:")
    task_list.append(new_task);
    return new_task

#method to remove old tasks that were completed
def subtractTask():
    old_task = input("What task would you like to remove: ")
    task_list.remove(old_task)
    return old_task

interface()
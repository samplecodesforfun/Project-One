#list that stores all our currently saved tasks
task_list = ["wake up","shower","go to work", "dinner", "sleep"]

#method to run the task program on the terminal
def interface():
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

#method to view the current list
def viewTaskList():
    for task in task_list:
        #takes the index of the task in the list and adds 1 to show its task # and task name and prints it
        print(int(task_list.index(task)+1), task)

# method to add new tasks to the list
def addTask():
    task_name = input("What task would you like to add:")
    #needs conditionals to stop if the number from going to the negatives
    task_number = int(input("What task # would you like to assign this task: "))
    task_list.insert(task_number-1,task_name)     
    

#method to remove old tasks that were completed
def subtractTask():
    old_task = input("What task would you like to remove: ")
    task_list.remove(old_task)
    return old_task


#viewTaskList()
#addTask()
#subtractTask()
interface()
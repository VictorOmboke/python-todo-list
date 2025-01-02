def get_task ():
    """
    Ask the user to enter a task that they would like to add to the todo list.

    Returns: task - return the task. 
    """
    task = input("Please enter a task. ")
    return task

def add_task (todo_list, task):
    """
    Add a new task to the todo list.

    Parameters:
    todo_list - the current list of tasks. 
    task - Serve as the task the user would like to add to the todo list.

    Returns: todo_list - updated todo_list with th new task added. 
    """
    #Append dictionary that holds task information and can be updated.
    todo_list.append({"Task": task, "Completed": False})
    print("Your task was added to the todo list.")
    return todo_list

def execute():
    """
    Call all functions and execute the apps behavior.
    """
    todo_list = []
    task = get_task()
    todo_list = add_task(todo_list, task)
    print("Current Tasks:", todo_list)

execute()

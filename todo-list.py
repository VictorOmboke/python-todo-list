def get_task ():
    """
    Ask the user to enter a task to be placed in the todo list.

    Returns: task - return the task. 
    """
    task = input("Please enter a task: ")
    return task

def add_task (todo_list, task):
    """
    Add a new task to the todo list.

    Parameters:
    todo_list - the current list of tasks. 
    task - Serve as the task the user would like to add to the todo list.

    Returns: todo_list - updated todo_list with the new task added. 
    """
    #Append dictionary that holds task information and can be updated.
    todo_list.append({"Task": task, "Completed": False})
    print(f"Your task '{task}' was added to the todo list.")

def get_more_tasks (todo_list):
    """
    Ask user if they would like to add more tasks to the todo list.

    Parameter: todo_list - current todo list

    Returns: nothing as we are modifying todo_list in place
    """
    # Initialize variable to enter the loop.
    prompt = "yes"
    while prompt == "yes":
        prompt = input("Would you like to add another task? (Enter 'Yes' or 'No'): ").lower()
        if prompt == "yes":
            new_task = get_task()
            add_task(todo_list, new_task)
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")
    

def execute():
    """
    Call all functions and execute the apps behavior.
    """
    todo_list = []
    # Get the first task
    task = get_task()
    # Add task to the todo list.
    add_task(todo_list, task)
    # Continue asking the user to enter more tasks if they would like.
    get_more_tasks(todo_list)
    # Display the current todo list.
    print("Todo List:")
    # Loop through todo list using enumerate to create a numbered list.
    for i, task_info in enumerate(todo_list, start=1):
        # Display list in an easily comprehensible format.
        print(f"{i}. {task_info['Task']} - Completed: {task_info['Completed']}")

execute()

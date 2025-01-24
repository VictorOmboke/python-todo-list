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
        elif prompt == "no" and len(todo_list) > 0:
            display_todo_list(todo_list)
        elif prompt == "no" and len(todo_list) == 0:
            print("Have a nice day!")
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")
            prompt = "yes"

def remove_task(todo_list):
    """
    Remove tasks from the todo list.

    Parameters: 
    todo_list - updated version of the todo list.
    index - the index of the task to be removed.

    Returns: Nothing as we are modifying the list.
    """
    prompt = "yes"
    while prompt == "yes":
        prompt = input("Would you like to remove a task from this list? (Enter 'Yes' or 'No'): ").lower()
        if prompt == "yes":
            index = int(input("Please enter the task number from the todo list. (Example: '1', '3', '4'): ")) - 1
            print(f"Your task '{todo_list[index].get("Task")}' was removed from the todo list.")
            todo_list.pop(index)
            if len(todo_list) > 0:  
                display_todo_list(todo_list)
            else:
                prompt = "no"
                print("Your todo list is empty.")
                get_more_tasks(todo_list)
        elif prompt == "no" and len(todo_list) > 0:
            display_todo_list(todo_list)
        elif prompt == "no" and len(todo_list) == 0:
            print("Have a nice day!")
        else:
            print("Invalid input, please enter 'Yes' or 'No'.")
            prompt = "yes"


def display_todo_list(todo_list):
    """
    Display the current todo list in a user friendly way.

    Parameters: todo_list - the updated todo list.
    """
    print("Todo List:")
    # Loop through todo list using enumerate to create a numbered list.
    for i, task_info in enumerate(todo_list, start=1):
        # Display list in an easily comprehensible format.
        print(f"{i}. {task_info['Task']} - Completed: {task_info['Completed']}")

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
    # Ask the user if they would like to remove any tasks.
    remove_task(todo_list)

execute()

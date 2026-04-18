def task():
    # Create an empty list to store tasks
    tasks = []

    # Display welcome message
    print("------ Welcome to the Task Manager App ------")

    # Ask user how many tasks they want to add initially
    total_task = int(input("Enter how many tasks you want to add: "))

    # Loop to take initial tasks from the user
    for i in range(1, total_task + 1):
        task_name = input(f"Enter Task {i}: ")
        tasks.append(task_name)  # Add task to the list

    # Display all tasks entered initially
    print("\nToday's Tasks:")
    for i, t in enumerate(tasks, 1):
        print(i, ".", t)

    # Infinite loop to keep showing menu until user exits
    while True:
        print("\nChoose an operation:")
        print("1 - Add Task")
        print("2 - Update Task")
        print("3 - Delete Task")
        print("4 - Display Tasks")
        print("5 - Exit")

        # Handle invalid (non-numeric) menu input
        try:
            operation = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        # Option 1: Add a new task
        if operation == 1:
            add = input("Enter the task you want to add: ")
            tasks.append(add)
            print(f"Task '{add}' added successfully.")

        # Option 2: Update an existing task
        elif operation == 2:
            updated_val = input("Enter the task name you want to update: ")

            if updated_val in tasks:
                new_task = input("Enter the new task name: ")
                ind = tasks.index(updated_val)  # Get index of task
                tasks[ind] = new_task          # Replace old task
                print("Task updated successfully.")
            else:
                print("Task not found!")

        # Option 3: Delete a task
        elif operation == 3:
            del_val = input("Enter the task name you want to delete: ")

            if del_val in tasks:
                ind = tasks.index(del_val)  # Find task index
                del tasks[ind]              # Delete task
                print("Task deleted successfully.")
            else:
                print("Task not found!")

        # Option 4: Display all tasks
        elif operation == 4:
            if not tasks:
                print("No tasks available.")
            else:
                print("\nYour Tasks:")
                for i, t in enumerate(tasks, 1):
                    print(i, ".", t)

        # Option 5: Exit the program
        elif operation == 5:
            print("Closing program... Goodbye!")
            break

        # If user enters a number outside 1–5
        else:
            print("Invalid choice! Please select between 1 and 5.")

# Call the function to start the program
task()

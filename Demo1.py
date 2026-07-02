tasks = []

while True:
    print("\n===== TO-DO APP =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print("\nTasks:")
        for task in tasks:
            print("-", task)

    elif choice == "3":
        break

    else:
        print("Invalid choice")
    print("Git is awsome!")
    print("This line is NOT staged")
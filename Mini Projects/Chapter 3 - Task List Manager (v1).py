tasks = []

def main():
    global tasks
    first_option = input("Would you like to:\n1. Add a task\n2. Remove a task\n3. View all tasks\n4 Exit Program\n")
    if first_option == "1" or first_option == "1.":
        tasks.append(f'{len(tasks) + 1}. {input("Enter a task: ")}')
        main()
    elif first_option == "2" or first_option == "2.":
        remove_index = int(input("Which task do you want to remove? "))
        if len(tasks) < remove_index:
            print("Invalid task!")
        else:
            del tasks[remove_index - 1]
            print("Successfully removed task!")
        main()
    elif first_option == "3" or first_option == "3.":
        if len(tasks) == 0:
            print("Tasks:")
            for task in tasks:
                print(task)
        else:
            print("You finished all your tasks! Great Job!")
        main()
    elif first_option == "4" or first_option == "4.":
        print("Thank you for using List Manager v1!")

if __name__ == "__main__":
    main()
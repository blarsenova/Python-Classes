inputAttempts = 0
tasks_list = []

while True:
    user_input = input("Enter your tasks in to-do list (or 'stop' or 'view'): ")
    inputAttempts += 1

    # Check for the stop words first
    if user_input == 'stop' or user_input == 'view':
        print('You asked to stop or view.')
        break # This exits the loop

    # If they didn't stop, add the task to our list
    tasks_list.append(user_input)
    print(user_input + ' is added task')

# After the loop ends, we handle the display
print(f"\n You have total of: {inputAttempts-1} tasks")
print("And these are all your tasks: " + str(tasks_list))
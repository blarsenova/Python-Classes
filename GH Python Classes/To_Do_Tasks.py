inputAttempts = 0

while True:
    user_input = input("Enter your tasks in to-do list (or 'stop' or 'view'): ")
    inputAttempts += 1

    # Check for the stop words first
    if user_input == 'stop' or user_input == 'view':
        print('You asked to stop or view.')
        break # This exits the loop

    # If they didn't stop, add the task to our list
   # tasks_list.append(user_input)
    #print(user_input + ' is added task')

# After the loop ends, we handle the display
#print(f"\n You have total of: {inputAttempts-1} tasks")
#print("And these are all your tasks: " + str(tasks_list))


#### Step 2: Write to the file

path = '/Users/baktygullarsenova/HelloWorld/Todo'
tasks_list = []
tasks_list.append(user_input)
#tasks_into_string= "\n".join(tasks_list)
f2 = open(path, 'a', encoding='utf-8')
f2.write("\n".join(tasks_list))
f2.close() # You MUST close it to save the changes before reading

# Step 3: Read from the file
try:
    with open(path, 'r', encoding='utf-8') as f:
        tasks_list = f.read().splitlines() # Loads old items into your list
except FileNotFoundError:
    tasks_list = [] # If file doesn't exist yet, start empty
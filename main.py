print("-"*35)
print("Welcome to your to-do list!")
# Add list:
to_do_list=[]
completed_tasks=[]
# Create while loop:
while True:
# Create a for loop to print index number & list:
    for i in range(len(to_do_list)):
            print(f"{i+1}- {to_do_list[i]}")
# Ask for user input:
    print("-"*35)
    print("Type in your task, or 'h' for help.")
    to_do_input = input("> ")
    print("-"*35)
# Option to exit loop: 
    if to_do_input == "q":
        break
# Add help option: 
    if to_do_input == "h":
        print("TO-DO LIST HELP:")
        print("Type 'q' to quit.")
        print("To add a task, type it and press enter.")
        print("To complete it, type its number and press enter.")
        print("-"*40)

# Add empty input handler:
    if len(to_do_input) == 0:
        print("Input can not be empty!")    
        print("-"*35)    
        exit()        
    
# Add option to input number to erase a completed task.
    elif to_do_input.isnumeric():
        number = int(to_do_input)
        if number > len(to_do_list):
            print("Sorry, there's no task with that number.") 
        else:
# Create variable to store task and pop it from to_do_list:
            task = to_do_list.pop(number-1)            
            completed_tasks.append(task)
# Add input to to_do_list:          
    else:
        to_do_list.append(to_do_input)
if completed_tasks:
    print(f"You completed ({len(completed_tasks)}) tasks today!")
# Add variable to count completed tasks:
    count = 1
    for to_do_list in completed_tasks:
        print(f"{count}- {to_do_list}")
        count += 1
    print("-"*35)
    print("Keep going!")
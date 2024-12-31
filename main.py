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
    elif to_do_input.isdgit() and 1 <= int(to_do_input) <=len(to_do_list):
        task_index = int(to_do_input) -1
        task = to_do_list.pop(task_index)
        completed_tasks.append(task)
        print(f"Task: {to_do_input}-{task}, marked as completed.")
        print("-"*35)

    elif to_do_input != "h" and to_do_input not in to_do_list:
        to_do_list.append(to_do_input)
        
if completed_tasks:
    print(f"You completed ({len(completed_tasks)}) tasks today!")
# Add variable to count completed tasks:
    count = 1
    for task in completed_tasks:
        print(f"{count} - {task}")
        count += 1
    print("-"*35)
    print("Keep going!")

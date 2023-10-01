# Create a simple to-do list program. The program should allow users to add tasks, mark tasks as completed, and view their to-do list.

# creaeting a structure for todo

todos = []

user_input = True

while user_input == True:
    
    user_choice = int(input('Enter the user choice\n 1. display all tasks. \n 2. add a task\n 3. mark a task as done. \n 4. exit\n'))
    match user_choice:
        case 1:
            print(todos)
        case 2:
            task_struc = {'task': '', 'completed': False}
            task = input('enter the task \n')
            task_struc['task'] = task
            todos.append(task_struc)
        case 3:
            task_num = int(input('enter the task number to mark as completed \n'))
            todos[task_num-1]['completed'] = True
        case 4:
            user_input = False
            
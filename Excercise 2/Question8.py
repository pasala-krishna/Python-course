# You are creating a task management application. Write a function filter_tasks that takes a list of tasks and a filtering function. It should return a new list containing tasks that meet the criteria specified by the filtering function.

def filter_tasks(tasks, filtering_function):
    
    filtered_tasks = []
    
    for task in tasks:
        if filtering_function(task):
            filtered_tasks.append(task)
    
    return filtered_tasks

# filtering functions

def completed_task(task):
    return task['status'] == 'completed'

def high_priority_task(task):
    return task['priority'] == 'high'

#  test case

tasks = [
    {'title': 'Task 1', 'status': 'completed', 'priority': 'high'},
    {'title': 'Task 2', 'status': 'in-progress', 'priority': 'medium'},
    {'title': 'Task 3', 'status': 'not-started', 'priority': 'low'},
    {'title': 'Task 4', 'status': 'completed', 'priority': 'low'},
    {'title': 'Task 5', 'status': 'not-started', 'priority': 'high'},
]
    
# filter completed tasks

completed_tasks = filter_tasks(tasks,completed_task)

# printing completed tasks
print('completed tasks are')
for task in completed_tasks:
    print(task, '\n')

# filter high priority tasks

high_priority_tasks = filter_tasks(tasks, high_priority_task)

# printing high priority tasks

print('high priority tasks are: ')

for task in high_priority_tasks:
    print(task, '\n')

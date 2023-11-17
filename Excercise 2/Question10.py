# You are building a time tracking app. Write a function total_time_worked that takes a list of time entries (start and end times) for tasks and calculates the total time worked.

def total_time_worked(time_entries):
    total_hours_worked = 0
    
    for entry in time_entries:
        
        start_time,end_time = entry
        
        total_hours_worked += end_time - start_time
    
    return total_hours_worked

# test cases

test_case1 = [(8, 12), (13, 17)]
result1 = total_time_worked(test_case1)

test_case2 = [(9, 10), (12, 13), (15, 17)]
result2 = total_time_worked(test_case2)

print("Test Case 1 - Total hours worked:", result1)
print("Test Case 2 - Total hours worked:", result2)
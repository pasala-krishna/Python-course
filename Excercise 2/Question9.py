# You are developing a calendar application. Write a function find_conflicts that takes a list of events (start and end times) and identifies any overlapping events.

def find_conflicts(events):
    conflicts = []
    # sort events by their start times
    events.sort(key = lambda event: event[0])
    
    for i in range(len(events) - 1):
        current_event = events[i]
        next_event = events[i+1] 
        
        # check for overlap
        
        if current_event[1] > next_event[0]:
            conflicts.append((current_event,next_event))
    
    return conflicts

# test cases:
events = [(9, 10), (9.30, 10.30), (10, 11)]
conflicts = find_conflicts(events)
print("Overlapping events:")
for conflict in conflicts:
    print(conflict)
'''- Input a list of Event objects, evaluate these objects' attributes to output a report of all users currently logged into a machine 
- To do this, check when users logged in and when (whether) they logged out 
- Make sure you process events in chronological order by sorting them by 
list.sort() method modifies original list 
sorted(list) returns a new list
For this problem, it's OK to modify the list so we will use list.sort()
key is a parameter that lets you use a function like len as the sorting parameter 
Planning:

If the event is a login, add the user to the list of users logged into that machine. If it's a logout, remove the user.
Use a set to store the users, adding at login and removing at logout. 
Store the sets in a dictionary with the machine name as the key and the set as a value. 
Have separate functions for processing the data vs for printing the report to the screen. '''

def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type = 'login':
            machines[event.machine].add(event.user)
        elif event.type = 'logout':
            if event.user in machines[event.machine]:
                machines[event.machine].remove(event.user)
    return machines

def generate_report(machines):
    for machine, usres in machines.items():
        # don't print a machine if no one is logged into it
        if len(users) > 0:
            user_list = ', '.join(users)
            print('{}: {}'.format(machine, user_list)

class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user 

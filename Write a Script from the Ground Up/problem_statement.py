# daily report that tracks the use of machines - which users are connected to which machines - records which users are logged into which machines at any given time

#input
#list of events - each event is an instance of the event class

"""
contains the date when the event happened, the name of the machine where it happened, the user, and the event type
"""
#in this scenario, we care about login and logout event types
#attributes are 
#Date
#User
#Machine
#Type - strings - we care about login and logout

#ouptput
"""
lists all machine names, and user currently logged in, prints information on the screen
"""
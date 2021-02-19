# what will we do for each event?
# when logged in, add to machine_users = []
# when logged out, remove from machine_users = []
# 
# use name of machine as a key and current users as the value:
# 
# for each event, we check if the machine is there.
# if it is, we update the entry
# if not, we create one
# 
# add user for logins, remove user for logouts

#afterward, we print a report of the information generated
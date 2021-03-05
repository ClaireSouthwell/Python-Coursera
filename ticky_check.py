#!/usr/bin/env python3 

import re
import operator # for sorting dictionaries by key
import csv
import sys

# REGEX
reg = r'ticky: (\w{4,5}) ([\w ]*) (\[#\d+\]\s)*\(([\w.]+)\)'
# Group 1: error.info; 2: message; 3: Ticket number; 4: username 

# DICTIONARIES 
per_user = {}
error = {}

#SYSLOG FILE
syslog =r"/home/student-00-565cdf4a2ebb/syslog.log"

def get_stats(logfile):
# Reading lines of the log file:
    with open(logfile, 'r') as file:
        for line in file.readlines():
            result = re.search(reg, line)
            name = result.group(4)
            ie = result.group(1)
            msg = result.group(2)
        # Add ALL messages to user statistics dictionary
            if name in per_user:
                if ie in per_user[name]:
                    per_user[name][ie] += 1
                else:
                    per_user[name][ie] = 1
            else:
                per_user[name] = {ie: 1}
        # Add errors to error dictionary 
            if ie == 'ERROR':
                if msg in error:
                    error[msg] += 1
                else:
                    error[msg] = 1
            

# Sort the dictionaries
    error = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
    per_user = sorted(per_user.items())

    return per_user, error

def make_csv(per_user, error):
# Write per_user to user_statistics.csv
    user_keys = ["Username", "INFO", "ERROR"]
    with open ('user_statistics.csv', 'w') as user_csv:
        writer = csv.writer(user_csv, fieldnames=user_keys)
        writer.writeheader()
        for item in per_user:
            user, log_type = item
            line = [user,log_type["INFO"],log_type["ERROR"]]                 
            writer.writerow(line)
    
# Write error to error_message.csv
    error_keys = ["Error", "Count"]
    with open ('error_message.csv', 'w') as error_csv:
        writer = csv.writer(error_csv, fieldnames=error_keys)
        writer.writeheader()
        writer.writerows(error)
                    

if __name__ == '__main__':
    per_user, error = get_stats(syslog)
    make_csv(per_user, error)
                    
                    


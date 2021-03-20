#!/usr/bin/env python3

import csv
import datetime
import requests


FILE_URL = "https://raw.githubusercontent.com/google/it-cert-automation-practice/master/Course4/Lab4/employees-with-date.csv"

def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)

def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""
    # Download the file over the internet
    response = requests.get(url, stream=True)
    lines = []
    # Decode the lines
    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    # Read them with csv reader; return this value for use in get_same_or_newer
    return csv.reader(lines[1:])

def get_same_or_newer(start_date):

    data = get_file_lines(FILE_URL)
    
    emp_dict = {}

    # Loop through the list of employees.
    # If they started on or after the given date, add them to emp_dict.
    
    for item in data:
        # Convert the date section of the string into a datetime object 
        item_date = datetime.datetime.strptime(item[3], '%Y-%m-%d')

        if item_date < start_date:
            continue

        if item_date >= start_date:
            if item_date in emp_dict:
                emp_dict[item_date].append("{} {}".format(item[0], item[1]))
            else:
                emp_dict[item_date] = ["{} {}".format(item[0], item[1])]
                
# Instead of returning a datetime object and a list of employees,
# this version returns one dictionary with datetime objects as keys
# and lists of employee names as values.

    return emp_dict

def print_results(d):
    '''Sort the dictionary by key and print the results in a sentence '''
    for i in sorted(d.keys()):
        print("Started on {}: {}".format(i.strftime("%b %d, %Y"), d[i]))

def main():
    start_date = get_start_date()
    results = get_same_or_newer(start_date)
    print_results(results)

if __name__ == '__main__':
    main() 

        

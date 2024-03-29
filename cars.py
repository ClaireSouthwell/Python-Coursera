#!/usr/bin/env python3

import json
import locale
import sys
import reports ######## Remember to add this!
import emails 

def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """

  # Establish the 3 criteria we are evaluating
  
  max_revenue = {"revenue": 0}
  max_sales = {'total_sales': 0}
  max_year = {'year': 1990, 'sales': 0}
  years = {}
  
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
      
      
    # TODO: also handle max sales
    item_sales = item['total_sales']

    if item_sales > max_sales['total_sales']:
      max_sales = item
    
    # TODO: also handle most popular car_year
    # Within this for loop we gather all the year data
    item_year = item['car']['car_year']

    if item_year in years:
      years[item_year] += item_sales
    else:
      years[item_year] = item_sales
      
  # Outside of the for loop that goes through all the cars,
  # we go through the dict of years and find the winner 
  for year, sales in years.items():
    if sales > max_year['sales']:
      max_year['year'] = year
      max_year['sales'] = sales
    

  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
    "The {} had the most sales: {}".format(
        format_car(max_sales['car']), max_sales['total_sales']),
    "The most popular year was {} with {} sales".format(
        max_year['year'], max_year['sales'])
  ]

  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]),
                       item["price"], item["total_sales"]])
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("car_sales.json")
  summary = process_data(data)
  new_summary = '<br/'.join(summary)
  print(summary)
  # TODO: turn this into a PDF report
  reports.generate("/tmp/cars.pdf", "Car Sales Statistics",
                   new_summary, cars_dict_to_table(data))

  # TODO: send the PDF report as an email attachment

  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Sales summary for last month"
  body = "{}\n{}\n{}".format(summary[0], summary[1], summary[2])
  message = emails.generate(sender, receiver, subject, body, "/tmp/cars.pdf")
  emails.send(message)




if __name__ == "__main__":
  main(sys.argv)

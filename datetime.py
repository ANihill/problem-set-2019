# Adam Nihill, 2019-03-20
# Program to that outputs today’s date and time in specific format
# Example Wednesday, March 20 at 18:24

import datetime

# Created a variable called today
# Set to current date and time 
today = datetime.datetime.now()

# Used strftime() Method to set format of date output
# https://www.w3schools.com/python/python_datetime.asp
print(today.strftime("%A, %B %d %Y at %H:%M"))
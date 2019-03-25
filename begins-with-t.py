# Adam Nihill, 2019-03-17
# Does this day begin with the letter "T"

# Call current date
import datetime
today = datetime.datetime.today().weekday()

# If current day is Tuesday or Thursday today begins with a "T" 
if today == 1:
  print("Yes - today begins with a T.")
elif today == 3:
  print("Yes - today begins with a T.")
else:
  print("No - today does not begin with a T.")

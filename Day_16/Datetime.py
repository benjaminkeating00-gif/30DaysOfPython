from datetime import *

my_date = datetime.now()
print("Current date and time:", my_date)
print("Year:", my_date.year)
print("Month:", my_date.month)  
print("Day:", my_date.day)
print("Hour:", my_date.hour)
print("Minute:", my_date.minute)
print("Second:", my_date.second)

formatted_date = my_date.strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted date and time:", formatted_date)

og_date_string = "Today is 5 December, 2019"
date_string = datetime.strptime(og_date_string, "Today is %d %B, %Y")
print("Parsed date:", date_string)

new_years = datetime(2026, 1, 1)

time_difference = new_years - my_date
print("Time until New Year's Day 2026:", time_difference)

long_frigging_time_ago = datetime(1970, 1, 1)
time_since = my_date - long_frigging_time_ago
print("Time since January 1, 1970:", time_since)


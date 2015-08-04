#!/usr/bin/python

# Check the time the person started working.
# Initialize a variable to keep track of the time.
# Check every two hours[1] to initialize the break.
# open browser
# repeat

# Code the function
# improve algorithm

# [1] Check literature for amount of breaks and time. more time worked,
# longer breaks needed.
import webbrowser
import time

total_breaks = 3
break_count = 0

url = 'https://www.youtube.com/watch?v=uQes2Bh9A3w'

print("This program started on " + time.ctime())

while break_count < total_breaks:
    time.sleep(10)               #<- in seconds - 2 hours = time.sleep(2*60*60)
    webbrowser.open_new_tab(url)
    break_count += 1
    

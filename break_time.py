# Check the time the person started working.
# Initialize a variable to keep track of the time.
# Check every two hours[1] to initialize the break.
# open browser
# repeat

# Code the function
# improve algorithm

# [1] Check literature for amount of breaks and time. more time worked,
# longer breaks needed.
import webbrowser, time

total_breaks = 3
break_count = 0

while break_count < total_breaks:
    time.sleep(5) #in seconds
    webbrowser.open('https://www.youtube.com/watch?v=uQes2Bh9A3w')
    break_count += 1
    #webbrowser.open_new_tab('http://www.google.com')

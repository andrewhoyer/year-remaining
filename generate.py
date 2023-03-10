import datetime
import math

current_date = datetime.date.today()
day_of_year  = (current_date.timetuple().tm_yday)

#day_of_year = 1 # For testing purposes. Set value from 1 to 365

if day_of_year >= 365:
    percent_remaining = 0.0
elif day_of_year == 1:
    percent_remaining = 100.0
else:
    percent_remaining = int((1 - (day_of_year / 365.0)) * 1000.0) / 10.0

# If percent remaining is less than 0.3 of any number, round it down and remove decimal.

if int(str(percent_remaining).split('.')[1]) < 3:
    percent_remaining = int(percent_remaining)

# Build a string that is the percentage rounded to the nearest 5

str_array = []
for ch in str(int(percent_remaining)):
    str_array.append(int(ch))

if str_array[-1] == 5 or str_array[-1] == 0:
    pass
elif str_array[-1] > 5:
    if len(str_array) > 1:
        str_array[-1] = 0
        str_array[-2] = str_array[-2] + 1
    else:
        str_array[-1] = 1
        str_array.append(0)
elif str_array[-1] < 5:
        str_array[-1] = 5

display_string = ''.join(map(str, str_array))

# Get the number of progress bar blocks on the left based on a 10-block format

blocks_out_of_ten = (100 - int(display_string)) / 10

# Determine the number of left / right progress bar blocks
# This allows for progress bars of varying length. Set bar_width to length of progress bar. 

bar_width        = 10
characters_left  = math.floor(blocks_out_of_ten * bar_width / 10.00)
characters_right = int(bar_width) - characters_left

# Build the progress bar text

progress_bar_array = []

counter = characters_left
while counter > 0:
    progress_bar_array.append('░')
    counter = counter - 1

counter = characters_right
while counter > 0:
    progress_bar_array.append('▓')
    counter = counter - 1

progress_bar_str = ''.join(progress_bar_array) + ' ' + str(percent_remaining) + '%'

output = [{'day_of_year': day_of_year, 'percent_remaining': percent_remaining, 'progress_bar_str': progress_bar_str}]

print(progress_bar_str)

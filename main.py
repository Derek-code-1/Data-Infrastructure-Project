#!/usr/bin/env python3
# Let's import a basic matplotlib
import matplotlib
matplotlib.use('TkAgg')  # Choose a GUI backend that usually shows windows
import matplotlib.pyplot as plt 

# Unbelievably simple first step: printing out sleep data.
# I have no idea how to even build a project, so this is literally scooping clay. 
# Not even making a brick yet, much less placing it down. 
# Here's my first line of code for this project; this is Day 1.
sleep_data = [5.0, 6.5, 7.0, 7.5, 8.0, 9.5, 6.5, 7.0, 4.5, 11.0]
print(sleep_data)
# That's it. No CSV, not even anything. That's just what I did: printed out a list.
# That's all I know how to do, so good enough for Day 1. 
# It's an iterative process, really. I don't even have a plan.
# Next step: let's make a Python script to calculate the average. This is step 0.0000002

total = 0.0
for sleep in sleep_data:
    total += sleep

average = total / len(sleep_data)
print(f"The average number of hours: {average}")
# Well, there's the average. I'm 1/1000000000th of the way there!
# At least I know what I'm doing so far, which is so much better than using AI to 
# generate 10,000 lines of code that I cannot fix by myself.
# Alright, I'll stop talking and continue with my micro-steps.

min = min(sleep_data)
max = max(sleep_data)

print(f"Min of the sleep: {min}")
print(f"Max of the sleep data: {max}")
print(f"Total amount of sleep I got: {total}")

if 'total' in globals():
    print("it is")

# plotting
x_val_min = 0
x_val_max = 0
for i in range(len(sleep_data)):
    if sleep_data[i] == min:
        x_val_min = i
    elif sleep_data[i] == max:
        x_val_max = i

y_val_min = min
y_val_max = max

days = []
for i in range(len(sleep_data)):
    days.append(i+1)
average_list = [average] * len(days)
# make sure good_sleep_line has the same length as days
good_sleep_line = [7] * len(days)

# Sleep data plot
plt.plot(days, sleep_data, marker = 'o', color = 'red', label = 'Actual Sleep Data')
plt.title(f"slepe over {len(days)} days")
plt.xlabel("days")
plt.ylabel("hours of sleep")

# Ideal sleep line plot
plt.plot(days, good_sleep_line, marker = 'o', color = 'blue', label = 'Ideal Sleep Line')
plt.text(x_val_max, y_val_max, "Max Value")
plt.text(x_val_min, y_val_min, "Min Value")

# Average sleep gotten line plot
plt.plot(days, average_list, marker = 'o', label = 'Average Sleep')
plt.grid()
plt.savefig("sleep_plot.png")
plt.legend()
plt.show()


print("HJI")
print("UPDATED CODE")
with open("metrics.txt", "a") as file:
    file.write(f"{average}\n")
    file.write(f"{min}\n")
    file.write(f"{max}\n")
# Load metrics from the file
with open("metrics.txt", "r") as file:
    lines = file.readlines()

# Display the contents
for line in lines:
    print(float(line.strip()))
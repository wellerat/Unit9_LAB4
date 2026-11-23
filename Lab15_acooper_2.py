"""
Program:  Plotting Cubic Numbers

Author: Ann Cooper

Purpose:  To work with matplotlib to gain experience using it.  The goal
          of this lab was to plot/graph the cube of each value.  First
          graph is only the values 1-5 but the second graph is the 
          cube values of 1-5000
          
Starter Code:  None but did import and use matplotlib.pyplot

Date: 11/19/2026
"""

import matplotlib.pyplot as plt

numbers = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 64, 125]

# Graphing/Plotting the first 5 Cubes

plt.figure()
plt.plot(numbers, cubes)
plt.title("First 5 Cubes")
plt.xlabel("Value")
plt.ylabel("Cube of Value")
plt.savefig("cubes_5.png")
plt.close()

# Graphing/Plotting 5000 Cubes

bigger_numbers = list(range(1, 5001))
bigger_cubes = []

for value in bigger_numbers:
    bigger_cubes.append(value ** 3)

plt.figure()
plt.plot(bigger_numbers, bigger_cubes)
plt.title("First 5000 Cubes")
plt.xlabel("Value")
plt.ylabel("Cube of Value")
plt.savefig("cubes_5000.png")
plt.close()

# Creating two graphs on one png file

plt.figure(figsize=(8,10))
plt.subplot(2,1,1)
plt.plot(numbers,cubes)
plt.title("First 5 Cubes")
plt.xlabel("Value")
plt.ylabel("Cube of Value")
plt.subplot(2,1,2)
plt.plot(bigger_numbers, bigger_cubes)
plt.title("First 5000 Cubes")
plt.xlabel("Value")
plt.ylabel("Cube of Value")
plt.savefig("cubes_combined.png")
plt.show()
plt.close()
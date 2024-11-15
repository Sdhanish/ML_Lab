import matplotlib.pyplot as plt
# Define x and y values
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]
# Create a line plot
plt.plot(x, y, marker='o', color='b', linestyle='-')
# Add title and labels
plt.title('Plot of y = x^2')
plt.xlabel('X values')
plt.ylabel('Y values')
# Display the grid
plt.grid(True)
# Show the plot
plt.show()

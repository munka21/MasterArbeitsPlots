import matplotlib.pyplot as plt

numberOfInstanzen = [10, 20, 50, 100]
runTimeOPT = [59.17, 1235.47, 79859.04, 16835609.43]
runTimeAlgo = [79.17, 235.47, 7859.04, 168309.43]


# Plot the bar graph
plot = plt.bar(numberOfInstanzen, runTimeOPT, runTimeAlgo)

# Add the data value on head of the bar
for value in plot:
    height = value.get_height()
    plt.text(value.get_x() + value.get_width() / 2.,
             1.002 * height, '%d' % int(height), ha='center', va='bottom')

# Add labels and title
plt.title("Bar Chart")
plt.xlabel("Year")
plt.ylabel("Unit")

# Display the graph on the screen
plt.show()
# A simple line graph
import matplotlib.pyplot as plt
squares = [1, 4, 9, 16, 25]
# fig : the entire figure or collection of plots
# ax : a single plot in the figure
fig, ax = plt.subplots() #generate one or more plots in the same figure
ax.plot(squares) # plot the data
plt.show() # open viewer and display the plot

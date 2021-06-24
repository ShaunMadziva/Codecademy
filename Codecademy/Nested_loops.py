sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  print(location)
  for element in location:
    #print(element)
    scoops_sold += element

print(scoops_sold)

# 1.
# We have provided the list sales_data that shows the numbers of different flavors of ice cream sold at three different locations: Scoopcademy, Gilberts Creamery, and Manny’s Scoop Shop.

# We want to sum up the total number of scoops sold. Start by defining a variable scoops_sold and set it to zero.

# Checkpoint 2 Passed
# 2.
# Loop through the sales_data list using the following guidelines:

# For our temporary variable of the for loop, call it location.
# print() out each location list.


# 3.
# Within our sales_data loop, nest a secondary loop to go through each location sublist element and add the element value to scoops_sold.

# By the end, you should have the sum of every number in the sales_data nested list.

# Print out the value of scoops_sold outside of the nested loop.
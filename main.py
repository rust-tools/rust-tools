# Import functions.py as cost
import functions as cost

# File Locations
itemsFile = r'data\items.json'
durabFile = r'data\rustlabsDurabilityData.json'

# Inputs
input1 = input("What do you want to raid? ")
input2 = input("What type of item is this? (B,V,D)? ")
input3 = input("What type of raid do you want to do? (eco/explo) ")


# Print the output of the function (pretty self explanatory)
if input2 == 'B':
    print(cost.findDurability('building', input1, input3))
elif input2 == 'V':
    print(cost.findDurability('vehicle', input1, input3))
elif input2 == 'D':
    print(cost.findDurability('deployable', input1, input3))
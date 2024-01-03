# Import functions.py as cost
import functions as cost

def console_calc():

    # Inputs
    input1 = input("What do you want to raid? ")
    input2 = input("What type of item is this? (B,V,D)? ")
    input3 = input("What type of raid do you want to do? (eco/explo) ")


    # Print the output of the function (pretty self explanatory)
    if input2 == 'B':
        print(cost.find_durability('building', input1, input3))
    elif input2 == 'V':
        print(cost.find_durability('vehicle', input1, input3))
    elif input2 == 'D':
        print(cost.find_durability('deployable', input1, input3))
        
if __name__ == "__main__":
    console_calc()
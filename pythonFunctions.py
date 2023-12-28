import json

def findID(filePath = r'data/items.json', search_term=None, search_by_id=False):
    """
    Finds the ID of an item based on the name or shortname of the item.
    If search_by_id is set to True, it will search by ID instead of name.

    Parameters:
    filePath (str): The path to the file containing the item data.
    search_term (str): The name or ID of the item to search for.
    search_by_id (bool): If True, will search by ID instead of name.

    Returns:
    info['name'] (str): The name of the item.
    id (str): The ID of the item.
    "Not a valid item name or id." (str): If no match is found.

    """
    
    # Open the file and load the data into a dictionary
    with open(filePath, 'r', encoding='utf-8') as f:
        data = json.load(f)  

    # Loop through the dictionary and return the ID if the search term matches 
    # the name or shortname of the item
    # If search_by_id is True, it will search by ID instead of name
    # If no match is found, it will return "Not a valid item name or id."   
    for id, info in data.items():
        if search_by_id:
            if id.lower() == search_term:
                return info['name']
            
        else:
            search_term = search_term.lower() 
            if info['name'].lower() == search_term:
                return id
            elif info['shortname'].lower() == search_term:
                    return id
                       
    return "Not a valid item name or id."


def findDurability(itemType: str, itemName: str, raidType: str = 'explo', durabFile: str = r'data/rustlabsDurabilityData.json'):
    """

    Finds the durability of an item based on the name, shortname or ID of the item.

    Parameters:
    durabFile (str): The path to the file containing the durability data.
    itemType (str): The type of item to search for. Valid options are 'deployable', 'vehicle' and 'building'.
    itemName (str): The name, shortname or ID of the item to search for.
    raidType (str): The type of raid to search for. Valid options are 'eco' and 'explo'.

    Returns:
    "Invalid Raid Type" (str): If the raid type is not valid.
    "Invalid Item Type" (str): If the item type is not valid.
    f"Trying to {raidType}raid: {itemName}<br>Best option to {raidType}raid: {key}<br>Cost: {value[-1]} sulfur<br>Time to raid: {value[3]}<br>Quantity needed: {value[1]}" (str): If the raid type is 'explo'.
    f"Trying to {raidType}raid: {itemName}<br>Best option to {raidType}raid: {key}<br>Time to {raidType}raid: {value[3]}<br>Quantity needed: {value[1]}" (str): If the raid type is 'eco'.

    """

    # Initialize variables
    raidTypeList = ['eco', 'explo']
    itemTypeList = ['deployable', 'vehicle', 'building']
    global itemsFile
    cheapest = float('inf')
    dict_ = {}
    list_ = []
    dellist = []

    # Open the file and load the data into a dictionary
    with open(durabFile, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Check if the raid type and item type are valid
    if raidType not in raidTypeList:
        return "Invalid Raid Type"
    if itemType not in itemTypeList:
        return "Invalid Item Type"

    # If the item type is deployable, search by ID
    if itemType == 'deployable':
        search_term = findID(itemsFile, itemName)
        returnName = findID(itemsFile, search_term, True)
    # If the item type is vehicle or building, search by name
    elif itemType == 'vehicle' or itemType == 'building':
        search_term = itemName.lower()
        returnName = itemName

    # Lots of for loops thx rustlabs
    # Loop through the dictionary and return the ID if the search term matches
    # the name or shortname of the item
    for info in data.values():
        for item, dictionary in info.items():
            if search_term.lower() == item.lower():
                for i in dictionary:
                    for key,value in i.items():
                        if key == "group":
                            list_.append(value)
                        if key == "toolId":
                            raidTool = findID(itemsFile, value, True)
                        elif key == "quantity":
                            list_.append(value)
                        elif key == "time":
                            list_.append(value)
                        elif key == "timeString":
                            list_.append(value)
                        elif key == "fuel":
                            list_.append(value)
                        elif key == "sulfur":
                            list_.append(value)
                    dict_[raidTool] = list_
                    list_ = []

    # If the raid type is eco, remove all items that are not melee
    if raidType == 'eco':
        for key,value in dict_.items():
            if value[0] != 'melee':
                dellist.append(key)
    # If the raid type is explo, remove all items that are not explosive
    elif raidType == 'explo':
        for key,value in dict_.items():
            if value[0] != 'explosive':
                dellist.append(key)

    # Delete the items that are not melee or explosive
    for i in dellist:
        del dict_[i]

    if itemType != 'vehicle':
        del dict_['Homing Missile']

    # If the raid type is explo, find the cheapest (sulfur) item to raid with
    if raidType == 'explo':
        for key, value in dict_.items():
            if value[-1] != None:
                if value[-1] < cheapest:
                    cheapest = value[-1] 

        # Return the cheapest item to raid with
        for key, value in dict_.items():
            if value[-1] == cheapest:
                return f"Trying to {raidType}raid: {returnName}<br>Best option to {raidType}raid: {key}<br>Cost: {value[-1]} sulfur<br>Time to raid: {value[3]}<br>Quantity needed: {value[1]}"
    
    # If the raid type is eco, find the cheapest (time) item to raid with
    elif raidType == 'eco':
        for key, value in dict_.items():
            if value[2] != None:
                if value[2] < cheapest:
                    cheapest = value[2]
        # Return the cheapest item to raid with
        for key,value in dict_.items():
            if value[2] == cheapest:
                return f"Trying to {raidType}raid: {returnName}<br>Best option to {raidType}raid: {key}<br>Time to {raidType}raid: {value[3]}<br>Quantity needed: {value[1]}"
            
def findRecycleOutput(itemName: str, recycleFile: str = r'data/rustlabsRecycleData.json'):
    global itemsFile
    with open(recycleFile, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for Id,datalist in data.items():
        x = findID(itemsFile, Id, True)
        if itemName.lower() == x.lower():
            print(x)
            for dictionary in datalist:
                recycleOutput = findID(itemsFile, dictionary['id'], True)
                probability = dictionary['probability']
                probability = "{:.0%}".format(probability)
                quantity = dictionary['quantity']
#FIXME: only outputs first 'recycle output' item, not everything
                return f"Trying to recycle: {itemName}<br>The output is: {quantity} {recycleOutput} with a {probability} probability."
            
# File Locations
itemsFile = r'data/items.json'
durabFile = r'data/rustlabsDurabilityData.json'
recycleFile = r'data/rustlabsRecycleData.json'
print(findRecycleOutput('Workbench Level 3'))
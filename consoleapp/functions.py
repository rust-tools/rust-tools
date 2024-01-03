import json

def find_id(
        file_path = r'data/items.json',
        search_term=None, 
        search_by_id=False):
    """
    Finds the ID of an item based on the name or shortname of the item.
    If search_by_id is set to True,
    it will search by ID instead of name.

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
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)  

    # Loop through the dictionary and return the ID,
    # if the search term matches the name or shortname of the item
    # If search_by_id is True, it will search by ID instead of name
    # If no match is found, it will return:
    # "Not a valid item name or id."   
    for id, info in data.items():
        if search_by_id:
            if id.lower() == search_term:
                return info['name']
        elif info['name'].lower() == search_term:
            return id
        elif info['shortname'] == search_term:
                return id
    return "Not a valid item name or id."


def find_durability(
        item_type: str, 
        item_name: str, 
        raid_type: str = 'explo', 
        durab_file: str = r'data/rustlabsDurabilityData.json'):
    """

    Finds the durability of an item based on the name,
    shortname or ID of the item.

    Parameters:
    durab_file (str): 
    The path to the file containing the durability data.

    item_type (str): 
    The type of item to search for. Valid options are:
    'deployable', 'vehicle' and 'building'.

    item_name (str): 
    The name, shortname or ID of the item to search for.
    raid_type (str): 
    The type of raid to search for. Valid options are:
    'eco' and 'explo'.

    Returns:
    "Invalid Raid Type" (str): 
    If the raid type is not valid.

    "Invalid Item Type" (str): 
    If the item type is not valid.

    f"Trying to {raid_type}raid: {item_name}
    \nBest option to {raid_type}raid: {key}
    \nCost: {value[-1]} sulfur
    \nTime to raid: {value[3]}
    \nQuantity needed: {value[1]}" (str): 
    If the raid type is 'explo'.

    f"Trying to {raid_type}raid: {item_name}\n
    Best option to {raid_type}raid: {key}\n
    Time to {raid_type}raid: {value[3]}\n
    Quantity needed: {value[1]}" (str): 
    If the raid type is 'eco'.

    """

    # Initialize variables
    raid_type_list = ['eco', 'explo']
    item_type_list = ['deployable', 'vehicle', 'building']
    global items_file
    cheapest = float('inf')
    dict_ = {}
    list_ = []
    dellist = []

    # Open the file and load the data into a dictionary
    with open(durab_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Check if the raid type and item type are valid
    if raid_type not in raid_type_list:
        return "Invalid Raid Type"
    if item_type not in item_type_list:
        return "Invalid Item Type"

    # If the item type is deployable, search by ID
    if item_type == 'deployable':
        search_term = find_id(items_file, item_name)
        return_name = find_id(items_file, search_term, True)
    # If the item type is vehicle or building, search by name
    elif item_type == 'vehicle' or 'building':
        search_term = item_name
        return_name = item_name

    # Lots of for loops thx rustlabs
    # Loop through the dictionary and return the ID 
    # if the search term matches
    # the name or shortname of the item
    for info in data.values():
        for item, dictionary in info.items():
            if search_term == item:
                for i in dictionary:
                    for key,value in i.items():
                        if key == "group":
                            list_.append(value)
                        if key == "toolId":
                            raidTool = find_id(items_file, value, True)
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
    if raid_type == 'eco':
        for key,value in dict_.items():
            if value[0] != 'melee':
                dellist.append(key)
    # If the raid type is explo, 
    # remove all items that are not explosive
    elif raid_type == 'explo':
        for key,value in dict_.items():
            if value[0] != 'explosive':
                dellist.append(key)

    # Delete the items that are not melee or explosive
    for i in dellist:
        del dict_[i]

    # If the raid type is explo, 
    # find the cheapest (sulfur) item to raid with
    if raid_type == 'explo':
        for key, value in dict_.items():
            if value[-1] != None:
                if value[-1] < cheapest:
                    cheapest = value[-1] 

        # Return the cheapest item to raid with
        for key, value in dict_.items():
            if value[-1] == cheapest:
                return 
            f"Trying to {raid_type}raid: {return_name}\nBest option to {raid_type}raid: {key}\nCost: {value[-1]} sulfur\nTime to raid: {value[3]}\nQuantity needed: {value[1]}"
    
    # If the raid type is eco, 
    # find the cheapest (time) item to raid with
    elif raid_type == 'eco':
        for key, value in dict_.items():
            if value[2] != None:
                if value[2] < cheapest:
                    cheapest = value[2]
        # Return the cheapest item to raid with
        for key,value in dict_.items():
            if value[2] == cheapest:
                return f"Trying to {raid_type}raid: {return_name}\nBest option to {raid_type}raid: {key}\nTime to {raid_type}raid: {value[3]}\nQuantity needed: {value[1]}"
            
# File Locations
items_file = r'data/items.json'
durab_file = r'data/rustlabsDurabilityData.json'
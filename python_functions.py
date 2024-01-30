import json

def find_id(
        file_path = r'data/items.json',
        search_term=None,
        search_by_id=False):
    """
    Finds the ID of an item based on the name or shortname of the item.
    If search_by_id is set to True, it will search by ID instead of name.

    Parameters:
    file_path (str): The path to the file containing the item data.
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

    # Loop through the dictionary and 
    # return the ID if the search term matches 
    # the name or shortname of the item
    # If search_by_id is True, 
    # it will search by ID instead of name
    # If no match is found, 
    # it will return "Not a valid item name or id."   
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


def find_durability(
        item_type: str, 
        item_name: str, 
        raid_type: str = 'explo',
        raid_tool: str = None, 
        durab_file: str = r'data/rustlabsDurabilityData.json'):
    """

    Finds the durability of an item based on the name, shortname or ID of the item.

    Parameters:
    durab_file (str): 
    The path to the file containing the durability data.

    item_type (str): 
    The type of item to search for. 
    Valid options are 'deployable', 'vehicle' and 'building'.

    item_name (str): 
    The name, shortname or ID of the item to search for.

    raid_type (str): 
    The type of raid to search for. 
    Valid options are 'eco' and 'explo'.

    Returns:
    "Invalid Raid Type" (str): 
    If the raid type is not valid.

    "Invalid Item Type" (str): 
    If the item type is not valid.

    f"Trying to {raid_type}raid: {item_name}<br>
    Best option to {raid_type}raid: {key}<br>
    Cost: {value[-1]} sulfur<br>Time to raid: {value[3]}<br>
    Quantity needed: {value[1]}" (str): If the raid type is 'explo'.

    f"Trying to {raid_type}raid: {item_name}<br>
    Best option to {raid_type}raid: {key}<br>
    Time to {raid_type}raid: {value[3]}<br>
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
    elif item_type == 'vehicle' or item_type == 'building':
        search_term = item_name.lower()
        return_name = item_name

    # Lots of for loops thx rustlabs
    # Loop through the dictionary and return
    # the ID if the search term matches
    # the name or shortname of the item
    for info in data.values():
        for item, dictionary in info.items():
            if search_term.lower() == item.lower():
                for i in dictionary:
                    for key,value in i.items():
                        if key == "group":
                            list_.append(('Group',value))
                        if key == "toolId":
                            raidTool = find_id(items_file, value, True)
                        elif key == "quantity":
                            list_.append(('Amount', value))
                        elif key == "time":
                            list_.append(('Time', value))
                        elif key == "timeString":
                            list_.append(('TimeString', value))
                        elif key == "fuel":
                            list_.append(('Lowgrade', value))
                        elif key == "sulfur":
                            list_.append(('Sulfur', value))
                    dict_[raidTool] = list_
                    list_ = []

    # If the raid type is eco, remove all items that are not melee
    if raid_type == 'eco':
        for key,value in dict_.items():
            if value[0][1] != 'melee':
                dellist.append(key)
    # If the raid type is explo, 
    # remove all items that are not explosive
    elif raid_type == 'explo':
        for key,value in dict_.items():
            if value[0][1] != 'explosive':
                dellist.append(key)

    # Delete the items that are not melee or explosive
    for i in dellist:
        del dict_[i]

    homing_list = ['Minicopter', 'Scrap Transport Helicopter', 'Attack Helicopter', 'Hot Air Balloon']

    # Remove Homing Missile if the item is not an airborn vehicle.
    if item_name.lower() not in homing_list:
        if 'Homing Missile' in dict_.keys():
            del dict_['Homing Missile']

    if raid_tool is not None:
        dellist = []
        for key in dict_.keys():
            if key.lower() != raid_tool.lower():
                dellist.append(key)
        for i in dellist:
            del dict_[i]
        if len(dict_) == 0:
            return "Invalid Raid Tool"
      
    # If the raid type is explo, 
    # find the cheapest (sulfur) item to raid with
    # if there are no sulfur items to raid with,
    # find the cheapest lowgrade item to raid with
    # this will only happen in the case that someone
    # is trying to raid with molotov or flamethrower
    if raid_type == 'explo':
        for key, value in dict_.items():
            if value[-1][1] != None:
                if int(value[-1][1]) < cheapest:
                    cheapest = value[-1][1]
                    cheapest_output = value[-1]
        if cheapest == float('inf'):
            for key, value in dict_.items():
                if value[-2][1] is not None:
                    if int(value[-2][1]) < cheapest:
                        cheapest = value[-2][1]
                        cheapest_output = value[-2]
        if raid_tool is None:
            # Return the cheapest item to raid with
            for key, value in dict_.items():
                if value[-1] or value[-2] is cheapest:
                    return f"Trying to {raid_type}raid: {return_name}<br>Best option to {raid_type}raid: {key}<br>Cost: {cheapest_output[1]} {cheapest_output[0]}<br>Time to raid: {value[3][1]}<br>Amount needed: {value[1][1]}"
        elif raid_tool is not None:
            return f"Trying to {raid_type}raid: {return_name}<br>Chosen option to {raid_type}raid: {key}<br>Cost: {cheapest_output[1]} {cheapest_output[0]}<br>Time to raid: {value[3][1]}<br>Quantity needed: {value[1][1]}"
    
    # If the raid type is eco, 
    # find the cheapest (time) item to raid with
    elif raid_type == 'eco':
        for key, value in dict_.items():
            if value[2][1] != None:
                if value[2][1] < cheapest:
                    cheapest = value[2][1]
        if raid_tool is None:
        # Return the cheapest item to raid with
            for key,value in dict_.items():
                if value[2][1] == cheapest:
                    return f"Trying to {raid_type}raid: {return_name}<br>Best option to {raid_type}raid: {key}<br>Time to {raid_type}raid: {value[3]}<br>Quantity needed: {value[1]}"
        elif raid_tool is not None:
            return f"Trying to {raid_type}raid: {return_name}<br>Chosen option to {raid_type}raid: {key}<br>Time to {raid_type}raid: {value[3]}<br>Quantity needed: {value[1]}"
            
def find_recycle_output(
        item_name: str, 
        recycle_file: str = r'data/rustlabsRecycleData.json'):
    """
    
    Finds the output of recycling an item based on the name, 
    shortname or ID of the item.

    Parameters:
    recycle_file (str):
    The path to the file containing the recycle data.

    item_name (str):
    The name, shortname or ID of the item to search for.

    Returns:
    f"{quantity} {recycleOutput} with a {probability} probability." (str):
    If the item is found.

    "Not a valid item name or id." (str):
    If the item is not found.

    """
    global items_file
    with open(recycle_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for Id,data_list in data.items():
        x = find_id(items_file, Id, True)
        if item_name.lower() == x.lower():
            for dictionary in data_list:
                recycle_output = find_id(items_file, dictionary['id'], True)
                probability = dictionary['probability']
                probability = "{:.0%}".format(probability)
                quantity = dictionary['quantity']
                yield f"{quantity} {recycle_output} with a {probability} probability."

def find_recycle_output_new(recycle_input: dict,
                            recycle_down_outputs: bool,
                            recycle_file: str = r'data/rustlabsRecycleData.json'
                            ):
    # input dict should be in the format of {item_id (or name, TBD): amount to be recycled}

#TODO: Add all items up at the end (so the output is not displaying the same item multiple times (except if the probability is not equal)
#TODO: Remove items from print that are recycled down (if recycle_down_outputs is True)

    final_products = ['High Quality Metal',
                      'Metal Fragments',
                      'Scrap',
                      'Cloth',
                      'Leather',
                      'Sulfur',
                      'Charcoal',
                      'Animal Fat']

    global items_file
    with open(recycle_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item, amount in recycle_input.items():
        for Id, data_list in data.items():
            x = find_id(items_file, Id, True)
            if item.lower() == x.lower():
                for dictionary in data_list:
                    recycle_output = find_id(items_file, dictionary['id'], True)
                    probability = dictionary['probability']
                    probability = "{:.0%}".format(probability)
                    quantity = dictionary['quantity']
                    quantity *= amount
                    yield f"{quantity} {recycle_output} with a {probability} probability."
                    if recycle_down_outputs:
                        if recycle_output in final_products:
                            continue
                        else:
                            yield from find_recycle_output_new({recycle_output: quantity}, recycle_down_outputs)


# File Locations
items_file = r'data/items.json'
durab_file = r'data/rustlabsDurabilityData.json'
recycle_file = r'data/rustlabsRecycleData.json'

test = find_recycle_output_new({'Targeting Computer': 2,
                                'Gears': 5}, True)
for i in test:
    print(i)
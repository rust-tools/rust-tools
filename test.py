import json
import pprint as pprint

# def findID(filePath):
#     name = input("Enter item name: ").lower()
#     with open(filePath, 'r', encoding='utf-8') as f:
#         data = json.load(f)
        
#     for id, info in data.items():
#         if info['name'].lower() == name:
#             return id
#         if info['shortname'] == name:
#             return id

#     return "Not a valid item name."

def findID(filePath, search_by_id=False):
    search_term = input("Enter item name or id: ").lower()
    with open(filePath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for id, info in data.items():
        if search_by_id:
            if id.lower() == search_term:
                return info['name']
        else:
            if info['name'].lower() == search_term:
                return id
            if info['shortname'] == search_term:
                return id

    return "Not a valid item name or id."

def findDurability(filePath, searchType=None):
    global itemsFile
    if searchType==None:
      searchType=='items'
    id = findID(itemsFile)
    with open(filePath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data[searchType][id]['durability']
    
# def findName(filePath, searchID):
#     with open(filePath, 'r', encoding='utf-8') as f:
#         data = json.load(f)
        
#     for id, info in data.items():
#         if id == searchID:
#             return info['name']

#     return "Not a valid ID."

itemsFile = r'Python\Rust-Raid-Calculator\Test\items.json'
durabFile = r'Python\Rust-Raid-Calculator\Test\rustlabsDurabilityData.json'

print(findID(itemsFile))
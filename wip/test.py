import json
import pprint as pprint

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
    for info in data.values():
        for item, dictionary in info.items():
            if item == id:
                return 'Item Found'
    

itemsFile = r'items.json'
durabFile = r'rustlabsDurabilityData.json'

print(findDurability(durabFile))
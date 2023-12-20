import json

# Load the data from the rustlabsDurabilityData.json file
with open('data/rustlabsDurabilityData.json', 'r') as f:
    data = json.load(f)

# Open the suggests.json file in append mode
with open('webapp/static/suggests.json', 'a') as f:
    # Iterate over the items in the data
    for item in data['items'].values():
        # Append each item to the suggests.json file
        for i in item:
            json.dump(i, f)
            f.write('\n')
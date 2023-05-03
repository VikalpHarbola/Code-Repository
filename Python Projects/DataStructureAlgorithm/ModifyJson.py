import json

# Load the existing JSON object into a Python variable
with open(r'C:\Dev_Space\Code-Repository\Python Projects\DataStructureAlgorithm\data.json', 'r') as f:
    data = json.load(f)

# Add a new key and value to the Python variable
data['messageKey'] = '12345'
data['processName']='abcdef'

# Convert the modified Python variable back into a JSON object
with open(r'C:\Dev_Space\Code-Repository\Python Projects\DataStructureAlgorithm\data.json', 'w') as f:
    json.dump(data, f)

# JSON Parsing 1


import json

# decodes the json file
output = json.load(open('cars.json'))

# display output to screen
# print output
print json.dumps(output, indent=4, sort_keys=True)

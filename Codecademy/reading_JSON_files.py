import json


#reading a JSON file (Javascript Object Notation)
with open("purchase.json") as purchase_json:
  purchase = json.load(purchase_json)       #parsing using json.load(), creating a Python dictionary out of the file
print(purchase['user'])
data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

import json


#write to a new JSON file
with open("data.json", "w") as data_json:
  json.dump(data_payload, data_json)     #json.dump() takes two arguments: first the data object, then the file object you want to save to.


#read the file
with open("data.json") as data_json:
  print(data_json.read())


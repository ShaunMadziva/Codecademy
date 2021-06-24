#import random


#try block 

caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

key_to_check = "matcha"
#caffeine_level["matcha"] = 30
try:
  print(caffeine_level[key_to_check])
except KeyError as k:
  print(str(k),"Unknown Caffeine Level")


#.get() dict.get(key) returns None if key not found

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)
print(tc_id)

stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)


#.pop dict.pop(key,default)

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)

health_points += available_items.pop("power stew", 0)

health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)


#dict_keys #list(dict) can also be used

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()

print(users)
print(lessons)


#dict values #list(dict.values()) can be used

um_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0 

for value in num_exercises.values():
  total_exercises += value

print(total_exercises)


#.items retursn a tuple (key, value)

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for key, value in pct_women_in_occupation.items():
  print(f"Women make up {value} percent of {key}s.")



tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}

spread["past"] = tarot.pop(13)
#print(spread)

spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)

for key, value in spread.items():
  print(f"Your {key} is the {value} card.")


# def tarot_card():
#   spread = {}
#   spread["past"] = tarot.pop(random.choice(list(tarot)))
#   spread["present"] = tarot.pop(random.choice(list(tarot)))
#   spread["future"] = tarot.pop(random.choice(list(tarot)))
#   for key, value in spread.items():
#     print("Your " + key +" is the " + str(value) + " card." )

# tarot_card()
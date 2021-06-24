user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

user_ids.update({"theLooper": 138475, "stringQueen": 85739})

print(user_ids)


oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = 9

print(oscar_winners)

#list comprehension with dictionsries (tuple unpacking)
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
#zipped_drinks_list = list(zipped_drinks)
#print(zipped_drinks_list)

drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine) 

#summary
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays ={key:value for key, value in zip(songs,playcounts)}



plays["Purple Haze"] = 1
plays.update({"Respect":94})
print(plays)


library = {"The Best Songs": plays, "Sunday Feelings":{}}

print(library )

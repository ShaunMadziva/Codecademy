#break

x = input("type: ")
items = ["shoes", "hat", "shirt", "hat", "cap"]
count = items.count(x)

for item in items:
    print(item)
    if item == x:
        print("Item(s) found")
        break
print("End of search!") 


#continue

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
  if age < 21:
    continue
  print(age)
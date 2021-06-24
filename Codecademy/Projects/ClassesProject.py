class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

  def __repr__(self):
    return f"Name: {self.name} \nFranchises: {self.franchises}"


class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def available_menus(self, time):
    available_menu = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menu.append(menu)
    return available_menu

  def __repr__(self):
    return f"Address: {self.address} \nMenu: {self.menus}"



class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def calculate_bill(self, purchased_items):
    bill = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill+=self.items[purchased_item]
    return bill
  
  def __repr__(self):
    return f"{self.name} menu is available from {self.start_time} to {self.end_time}"

#brunch menu
items1 = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch = Menu("brunch", items1, 1100, 1600)

#early_bird menu
items2 = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird = Menu("early_bird", items2, 1500, 1800)


#dinner menu
items3 = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner = Menu("dinner", items2, 1700, 2300)


#kids menu
items4 = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids = Menu("kids", items4, 1100, 2100)

#arepas_menu
arepas_menu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepa = Menu("Arepa", items4, 1000, 2000)

menus = [brunch, early_bird, dinner, kids]


#print(brunch)

break_fast = ["pancakes", "home fries", "coffee"]
#print(brunch.calculate_bill(break_fast))

lunch = ["salumeria plate", "mushroom ravioli (vegan)"]
#print(early_bird.calculate_bill(lunch))

flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

#print(flagship_store)

a = flagship_store.available_menus(1700)
#print(a)

first_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
#print(first_business)

arepas_place = Franchise("1232 West End Road", arepa)
#print(arepas_place)

new_business = Business("Take a' Arepa", arepas_place)
print(new_business)
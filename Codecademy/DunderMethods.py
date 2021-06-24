class Atom:
  def __init__(self, label):
    self.label = label
  def __add__(self, other):
    return Molecule([self, other])
    
class Molecule:
  def __init__(self, atoms):
    if type(atoms) is list:
	    self.atoms = atoms
  def __repr__(self):
    molecular_formula = ""
    for index in range(len(self.atoms)):
      molecular_formula += salt.atoms[index].label
    return molecular_formula
      
sodium = Atom("Na")
chlorine = Atom("Cl")
#salt = Molecule([sodium, chlorine])
salt = sodium + chlorine

print(salt)


#Dunder Methods II
class LawFirm:
  def __init__(self, practice, lawyers):
    self.practice = practice
    self.lawyers = lawyers
  
  def __len__(self):
    return len(self.lawyers)

  def __contains__(self, lawyer):
    contain = lawyer in self.lawyers
    return contain

  def __repr__(self):
    return str(len(self.lawyers))
    
d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])

print(d_and_p)

if "Donelli" in d_and_p:
  print(True)


#subclass of the list class that appends in sorted 
class SortedList(list):
  def __init__(self, list):
    super().__init__(list)
    self.sort()
  def append(self, value):
    super().append(value)
    self.sort()

a = SortedList([4, 1, 5])
#a.append(10)
print(a)


#modify dict to return a fallback value when key not found
class NewDic(dict):
  def get(self, key):
    super().get(key)
    if key not in self.keys():
      return "this is not the answer"
    else:
      return self[key]

# new_dic = NewDic({42: 'this is the answer', })
# printnew_dic(new_dic.get(41))
# print(new_dic.get(42))

# dic ={"key":"value"}
# print(dic.get("skey"))
# print(dic.get('key'))
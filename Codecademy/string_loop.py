#calculate length of word
def get_length(string):
  length = 0
  for letter in string:
    length += 1
  return length

len_my_name = get_length("Shaun")
print(len_my_name)

#check if letter is in word
def letter_check(word, letter):
  for val in word:
    print(val)
    if val == letter:
      return True
  return False
    
print(letter_check("strawberry", "a"))
print(letter_check("strawberry", "o"))

# def contains(big_string, little_string):
#   return little_string in big_string 

# print(contains("watermelon", "melon"))


#returns a list with all of the letters they have in common.
def common_letters(string_one, string_two):
  common = []
  for x in string_one:
    print(x)
    if x in string_two and x not in common:
       common.append(x)

print(common_letters('manhattan', 'san francisco'))


def password_generator(username): 
  password = ""
  for index in range(0,len(username)):
    password += username[index -1]
  return password

print(password_generator("AbeSimp"))
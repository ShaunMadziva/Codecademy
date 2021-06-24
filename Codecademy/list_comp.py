# numbers = [2, -1, 79, 33, -45]
# doubled = []
 
# for number in numbers:
#   doubled.append(number * 2)
 
# print(doubled)


#new_list = [<expression> for <element> in <collection>]
numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers]
print(doubled)



# from random import randint

# random_numbers = [ randint(number, 2 * number) for number in range(10)]

# print(random_numbers)


#List Comprehensions: Conditionals
# numbers = [2, -1, 79, 33, -45]
# only_negative_doubled = []
 
# for num in numbers:
#   if num < 0: 
#     only_negative_doubled.append(num * 2)
 
# print(only_negative_doubled) 

#if
numbers2 = [2, -1, 79, 33, -45]
negative_doubled = [num * 2 for num in numbers2 if num < 0]
print(negative_doubled)

#if else
# numbers = [2, -1, 79, 33, -45]
# doubled = [num * 2 if num < 0 else num * 3 for num in numbers ]
# print(doubled)
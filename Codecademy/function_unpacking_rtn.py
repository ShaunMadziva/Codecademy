#Unpacking Multiple returns
def scream_and_whisper(text):
    scream = text.upper()
    whisper = text.lower()
    return scream, whisper

the_scream, the_whisper = scream_and_whisper("help")

print(the_scream)
print(the_whisper)

#we use a single asterisk (*) to indicate we’ll accept any number of positional arguments
def shout_strings(*args): 
  for argument in args:
    print(argument.upper())
 
shout_strings("hi", "what do we have here", "cool, thanks!")  
# Prints out:
# "HI"
# "WHAT DO WE HAVE HERE"
# "COOL, THANKS!"


print("My name is {name} and I'm feeling {feeling}.".format(name="Shaun", feeling="Happy"
	# add your arguments to .format()
))


from products import create_product

# Update create_products() to take arbitrary keyword arguments
def create_products(**kwargs):
  for name, price in kwargs.items(): #dictionary
    create_product(name, price)

# Update the call to `create_products()` to pass in this dictionary as a series of keyword
create_products(Baseball=3, Shirt=14, Guitar=70)

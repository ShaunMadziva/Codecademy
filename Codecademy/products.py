def create_product(name, price):
  print("{} created, being sold for ${}".format(name, price))

def find_string(**kwargs):
    for keyword, arg in kwargs.items():
        print(arg.find(keyword))

find_string(a="shaun madziva")



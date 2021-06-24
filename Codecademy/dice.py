# Import random below:
import random

#print(dir(random))
#help(random)

# Create random_list below:
random_list = [random.randint(1,12) for num in range(13)]
#coin = ["heads", "tails"]
# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)

#random.sample()
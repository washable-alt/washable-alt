import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

random_side = random.randint(0, 1)

#print head if value equals to 1, otherwise, print "Tails"
if random_side == 1:
    print("Heads")
else:
    print("Tails")


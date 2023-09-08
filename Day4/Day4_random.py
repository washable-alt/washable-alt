import random
import Day4_my_module
#using random module
#calling a custom module on another file; printing the pi variable value

random_integer = random.randint(1,10)

print(random_integer)

#0.0000000-0.999999...
random_float = random.random() 

print(random_float)

print(Day4_my_module.pi)

# Create a random decimal number between 0 and 5
# 0.000000 - 4.9999999
random_float *= 5
print(random_float)

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")
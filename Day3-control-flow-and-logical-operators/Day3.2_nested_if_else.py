"""
if condition:
    if another condition:
        do this
    else:
        do this
else:
    do this
"""
# Ask for input in height
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


# Ask what is your age if height is above 120cm. Check age if it is less than 12, less than 18. 
# If more than 18, pay $12

if height >= 120: 
    print("You can ride the rollercoaster! ")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5. ")
    elif age <= 18:
        print("Please pay $7. ")
    else:
        print("Please pay $12. ")
else:
    print("Sorry, you have to grow taller before you can ride.")
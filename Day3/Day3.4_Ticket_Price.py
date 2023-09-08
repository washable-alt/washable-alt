height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))

    if age < 12: 
        price = 5
        print(f"Child tickets are ${price}. ")
    elif age <= 18:
        price = 7
        print(f"Youth tickets are ${price}. ")
    else: 
        price = 12
        print(f"Adult tickets are ${price}. ")
    
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        price += 3

    print(f"Your final bill is ${price}. ")

else:
    print("Sorry, you have to grow taller before you can ride.")
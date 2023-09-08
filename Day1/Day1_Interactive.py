#printing statements to console

print("Day 1 - Python Print Function")

print("The function is declared like this: ")

print("print('what to print')")

#debugging 

print("Day 1 - String Manipulation")
print("String Concatenation is done with a '+' Sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# Switching variables

a = input("a:")
b = input("b:")

# Assign the value of b to a and value of a to b

tmp=a
a = b
b = tmp

print('a = ' + a)
print('b = ' + b)

#BandName Generator

#Create a greeting for your program 
print("Welcome to the Band Name Generator.\n")

#Ask the user for the city that they grew up in
city_name = input("What's the name of the city you grew up in?\n")

#Ask the user for the name of a pet
pet_name = input("What's your pet's name?")


# Combine the name of their city and pet and show them their band name
band_name = "Your band name could be {} {}\n"
print(band_name.format(city_name, pet_name))


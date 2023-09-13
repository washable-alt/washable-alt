# Dictionary - group and tag related information - {key:value} pair

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop":"The action of doing something over and over again."
}


# To print out the value of the programming dictionary, 
print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])
print(programming_dictionary["Loop"])

# Adding new items to dictionary
programming_dictionary["Algorithm"] = "A set of instructions that are followed to solve a problem."

print(programming_dictionary)

#Initialize an empty list
empty_list = []

#Initialize an empty dictionary

empty_dictionary = {}

# Wipe an existing dictionary 
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary 
programming_dictionary["Bug"] = "A moth in your computer."

# Loop through a dictionary
for key in programming_dictionary:
    # output is a key
    print(key)
    # print value
    print(programming_dictionary[key])


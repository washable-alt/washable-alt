year = input("Which year do you want to check? ")

#try-except-else block

# try: 
#     #execute this block
#
# except (TypeError/ValueError or other kinds of exception errors and try to catch them):
#   print("Wrong variable type!")
# else: 
#   execute this block if no exceptions are found

try:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year.")
            else:
                print("Not leap year.")
        else:
            print("Leap year.")
    else:
        print("Not leap year.")

# Exception is encountered thus it will print out wrong variable type. 
except TypeError as error:
    print("An error occurred:", type(error).__name__, "-", error)
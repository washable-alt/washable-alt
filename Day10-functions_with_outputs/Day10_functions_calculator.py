from art import logo

print(logo)

#Calculator 

def add(num_one, num_two):
    return num_one + num_two

def subtract(num_one, num_two):
    return num_one - num_two

def multiply(num_one, num_two):
    return num_one * num_two

def divide(num_one, num_two):
    return num_one / num_two

# Initialize a dictionary containing symbol as key and operation as value
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Ask for input for first number

num_one = int(input("What's the first number?: "))
num_two = int(input("What's the second number?: "))

for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
calculation_function = operations[operation_symbol]
first_answer = calculation_function(num_one,num_two)

print(f"{num_one} {operation_symbol} {num_two} = {first_answer}")

operation_symbol = input("Pick another operation: ")
num_three = int(input("What's the next number?: "))
calculation_function = operations[operation_symbol]
second_answer = calculation_function(calculation_function(num_one, num_two), num_three)
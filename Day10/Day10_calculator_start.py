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
def calculator():
    num_one = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num_two = float(input("What's the second number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num_one,num_two)

        print(f"{num_one} {operation_symbol} {num_two} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}: ") == "y":
            num_one = answer
        else:
            should_continue = False
            calculator()

calculator()

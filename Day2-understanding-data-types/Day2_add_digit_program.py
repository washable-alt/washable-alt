# Goal - Write a program that adds the digit in a 2 digit number. e.g. if the input is 35, it should give the result of 8. (3+5)

def get_two_digit_number(prompt):
    while True:
        try:
            value=input(prompt)
    
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if len(value) !=2:
            print("Sorry, your response is not 2 digit number.")
            continue
        else:
            break
    return value

def addition_within_two_digit_number(value):
    first_digit = value[0]
    second_digit = value[1]

    result=int(first_digit) + int(second_digit)
#    print(first_digit)
#    print(second_digit)
    return result

two_digit_number=get_two_digit_number("Type a two digit number: ")
add_result=addition_within_two_digit_number(two_digit_number)
print("The addition result of the digits in a 2 digit number is {}".format(add_result))
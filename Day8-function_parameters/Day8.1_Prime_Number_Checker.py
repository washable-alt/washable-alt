# To create a prime number checker
# A prime number is one that is divisible by one or itself but not any other numbers

n = int(input("Check this number: "))

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        #print(i)
        if number % i == 0:
            #not a prime
            is_prime = False
    if is_prime:
        print("It's a prime number. ")
    else:
        print("It's not a prime number. ")


prime_checker(number=n)


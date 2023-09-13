def add(*args):
    print(args[1])

    sum = 0

    for n in args:
        sum += n
    return sum

print(add(3,5,6,2,1,7,4,3))

def multiply(*args):
    
    sum=1
    
    for n in args:
        sum *= n
    return sum

print(multiply(3,5,6,2,1,7,4,3))

def calculate(n, **kwargs):
    print(kwargs)
    #for key, value in kwargs.items():
    #    print(key)
    #    print(value)
    # {'add' : 3, 'multiply': 5}
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

result = calculate(2, add=3, multiply=5)
print(result)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
print(my_car.color)
# An object is combining attributes and methods 
# Multiple versions of the same objects 
# Blueprint - Individual objects - known as class
# OOP vs procedural programming

# Object to a class
# car = CarBlueprint()

from turtle import Turtle, Screen
from prettytable import PrettyTable, from_csv

def turtle_move():
    timmy = Turtle()
    print(timmy)
    timmy.shape("turtle")
    timmy.color("coral")
    timmy.speed(1)
    timmy.forward(100)
    timmy.right(45)
    timmy.forward(100)
    timmy.left(45)
    timmy.forward(100)
    timmy.left(45)
    timmy.forward(100)
    timmy.left(90)
    timmy.forward(100)
    timmy.left(45)
    timmy.forward(100)
    timmy.left(45)
    timmy.forward(100)
    timmy.left(135)

    # toa cah soh
    timmy.forward(341.421356237)
    timmy.left(90)
    radius = 220.710678119
    timmy.speed(0)
    for i in range(100):
        timmy.circle(radius + i, 360)


    my_screen = Screen()
    print(my_screen.canvheight)
    my_screen.exitonclick()


def pretty_table(): 
    #x = PrettyTable()

    #x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
    #x.add_rows(
    #    [
    #        ["Adelaide", 1295, 1158259, 600.5],
    #        ["Brisbane", 5905, 1857594, 1146.4],
    #        ["Darwin", 112, 120900, 1714.7],
    #        ["Hobart", 1357, 205556, 619.5],
    #        ["Sydney", 2058, 4336374, 1214.8],
    #        ["Melbourne", 1566, 3806092, 646.9],
    #        ["Perth", 5386, 1554769, 869.4],
    #    ]
    #)

    #y = PrettyTable()

    #y.field_names = ['row ID','Location','MinTemp','MaxTemp','Rainfall','Evaporation','Sunshine','WindGustDir'
    #                 ,'WindGustSpeed','WindDir9am','WindDir3pm','WindSpeed9am','WindSpeed3pm','Humidity9am','Humidity3pm'
    #                 ,'Pressure9am','Pressure3pm','Cloud9am','Cloud3pm','Temp9am','Temp3pm','RainToday','RainTomorrow',]

    #with open("insert file path",'r') as fp:
    #    mytable = from_csv(fp)
    #print(mytable)
    #
    #data = mytable.get_string()
    #try: 
    #    with open('insert file path', 'w',encoding='utf-8') as f:
    #        f.write(data)
    #        f.close()
    #except Exception as e:
    #    print(e)

    table = PrettyTable()
    table.add_column("Pokemon Name", ["Pikachu", "Squirtle","Charmander"])
    table.add_column("Type", ["Electric", "Water","Fire"])

    # Default align is center, denoted by 'c'; align is one of the attributes
    print(table.align)
    table.align = 'l'
    print(table.align)
    print(table)


    
if __name__ == "__main__":
    pretty_table()
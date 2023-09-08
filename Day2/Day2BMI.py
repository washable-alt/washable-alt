# BMI Calculator

height=input("enter your height in m:\n")
weight=input("enter your weight in kg:\n")

#2 is an integer but height is a str, so there is a need to change the height variable type to float, as height has decimal places

bmi = int(weight) / float(height) ** 2
print(bmi)
bmi_as_int=int(bmi)

# improvements would be to consider the ranges the user may input 
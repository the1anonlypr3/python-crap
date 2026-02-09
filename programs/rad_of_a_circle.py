import math

radius_sq = int(input("radius: "))
unit = input("measurement unit: ")
plcs = int(input("rounded to x decimal places?: "))
A = math.pi * radius_sq ** 2 

if unit == "":
    print(f"The area of the circle is {A}")
else:
    print(f"The area of the circle is {round(A, plcs)}{unit}^2")
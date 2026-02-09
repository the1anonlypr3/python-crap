import math

a = int(input("enter a: "))
b = int(input("enter b: "))
unit = input("measurement unit?: ")
plcs = int(input("rounded to x decimal places?: "))
c = round(math.sqrt(pow(a, 2) + pow(b, 2)), plcs)

print(f"your hypotenuse (c): {c}{unit}! you're welcome")
temp = float(input("enter temp: \n"))
unit = input("enter unit: \n").lower()

if unit in ("c", "celcius", "better unit"):
    print(f"{temp}{unit} is {round(temp * 1.8 + 32, 2)}F")
elif unit in ("f", "fahrenheit", "shit unit"):
    print(f"{temp}{unit} is {round((temp - 32) / 1.8, 2)}C")
else:
    print(f"{unit} is a bullshit unit, run again")
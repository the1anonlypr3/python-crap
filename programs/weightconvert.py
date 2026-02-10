weight = float(input("enter weight: \n"))
unit = input("unit? (lb, kg): \n").lower()

if unit in ("lb", "lbs"):
    print(f"\n{weight}{unit} converts to {round(weight / 2.205, 2)}kg.")
elif unit in ("kg", "kgs"):
    print(f"\n{weight}{unit} converts to {round(weight * 2.205, 2)}lb.")
else:
    print(f"{unit} isn't valid ya itchbay")

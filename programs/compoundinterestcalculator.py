p = 0
r = 0
t = 0

while p <= 0 or r <= 0 or t <= 0:
    p = float(input("principle value (can't be greater than or less than 0):\n"))
    r = float(input("interest rate (can't be greater than or less than 0):\n"))
    t = int(input("time? (years, can't be greater than or less than 0):\n"))

print(f"balance after {t} years, with a principle balance of ${p:,.2f} and an interest rate of {r:,.2f}%:\n${p * pow((1 + r / 100), t):,.2f}")

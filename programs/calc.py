op = input("enter operator: ")
num1 = int(input("num1: "))
num2 = int(input("num2: "))

if op == "*":
    answer = num1 * num2 
elif op == "/":
    answer = num1 / num2 
elif op == "+":
    answer = num1 + num2 
elif op == "-":
    answer = num1 - num2 

if op == "+" and num1 == 9 and num2 == 10:
    print("21")
    quit()

print(answer)
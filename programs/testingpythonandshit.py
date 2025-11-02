# robot barista!! :3
import time
print("hiii :D")
name = input("whats your name? :3 ")

if name == "Ben" or name == "Patricia":
    evil = input("are you evil " + name + "? (y/n) ").lower()
    if evil == "y":
        deeds = int(input("how many good deeds have you done today? "))
        if evil == "yes" and deeds > 4:
            print("come in!")
            
        elif deeds < 4:
            print("not good enough! leave >:(")
            exit()
else:
    print("hiya non-evil", name, "thanks for coming in!")

menu = "networkchuck coffee, networkchuck croissant, networkchuck milkshake"
price = 8
print(f"our menu for today is {menu}.\n")
order1 = input("what would ya like? ")
order = int(input("awesome! how many? "))
print(f"ok coolsies!", name, "that'll be $", order * price, " please!")
answer = input("all good with you? ")
if answer == "no":
    print("ah alright, goodbye then <3")
else:
    print(f"wonderful {name}, your",  order, order1 + "s will be ready soon!")


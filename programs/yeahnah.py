# yeah nah generator
import random

yeahnah = ["yeah ", "nah "]

def yeahnahgen():
    yeahnahpool = ""
    user_input = int(input("how many yeah nahs? > "))
    for _ in range(user_input):
        yeahnahpool += random.choice(yeahnah) 
    print(yeahnahpool)

while True:
    yeahnahgen()
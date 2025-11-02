print("welcome to my really cool averageanator, which actually gets the average of numbers believe it or not \n")

def average():
    numlist = []
    nums = int(input("how many numbers?: "))
    for i in range(nums):
        numinput = int(input("number: "))
        numlist.append(numinput)
    total = sum(numlist)
    avg = total / len(numlist)
    print(f"average: {avg}")

average()
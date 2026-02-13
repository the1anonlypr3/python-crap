# no more than 12 chars
# no spaces
# can't contain digits

u = input("hi twin enter a username\n(can't be more than 12 chars, no spaces, no numbers):\n")

if len(u) > 12:
    print("name too long.")
elif u.count(" ") >= 1:
    print("can't contain spaces")
elif not u.isalpha():
    print("cant have nums cunt")
else:
    print(f"welcome {u}")
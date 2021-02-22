#numero narcisista

num = input()
po = len(num)
tot = 0
for i in num:
    tot += int(i)**po
print("true" if int(num) == tot else "false")

# 	Goal
# Read the characters from the standard input and print them in the requested order. The order is given as a series of digits describing the position in the original input string of the next character to print.
# Input
# Line 1: n
# Line 2: n characters
# Line 3: n unique digits in the range 1..n
# Output
# n characters in the requested order
# Constraints
# 1 ≤ n ≤ 9
# Example
# Input
# 4
# abcd
# 4 3 2 1

# n = int(input())
n=4
# line = input()
line="abcd"
# for i in input().split():
#     index = int(i)
index=[4,3,2,1]
ou=""
for ct in index:
    ou=ou+str(line[ct-1])
print(ou)

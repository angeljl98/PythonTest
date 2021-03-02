# You must output the sum of the digits of the exponentiation of two input numbers.
#
# Example:
#
# Input:
# 2
# 7
#
# Output:
# 11
# Input
# Line 1: An integer X for the base.
# Line 2: An integer Y for the exponent.
# Output
# A single line containing the sum of all digits from the result of X^Y
# Constraints
# 0 ≤ X ≤ 15
# 0 < Y ≤ 11
# Example
# Input
# 5
# 2
# Output
# 7

x = int(input())
y = int(input())
z = str(x**y)
s = 0
for i in range(len(z)):
    s += int(z[i])
print(s)

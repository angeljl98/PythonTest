# Goal
# You are given integers n and m.
# You need to find out if the digitwise products modulo 43
# are the same for both of them.
#
# The digitwise product of a number is all digits of a number multiplied together.
# For example, the digitwise product of 95 would be: 9 * 5 = 45.
# The modulo operation returns the remainder or signed remainder of a division.
# For our example, it would be: 45 mod 43 = 2,
# so we see that the digitwise product of 95 mod 43 would be 2.
# Input
# Line 1: The integer n.
# Line 2: The integer m.
# Output
# Line 1: One of the digitwise products modulo 43
# if the two digitwise products are the same modulo 43, and -1 otherwise.
# Constraints
# 0 ≤ n, m < 2^32
# Example
# Input
# 436
# 89
# Output
# 29

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def px(x):
    y=str(x)
    z=1
    for i in y:
        z=z*int(i)
    return z

n = int(input())
m = int(input())
v1=px(n)%43
v2=px(m)%43
if (v1==v2):
    print(str(v1))
else:
    print("-1")

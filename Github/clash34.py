# The program:
# You will be given a positive integer N as input.
# Print the factorial of N.
#
# INPUT:
# Line 1 : N the integer.
#
# OUTPUT:
# N!, the factorial of N.
#
# CONSTRAINTS:
# 0 < N ≤ 12
#
# EXAMPLE:
# Input
# 4
# Output
# 24

import sys
import math

n = int(input())
fact = 1

for i in range(1,n+1):
    fact = fact * i

print(fact)

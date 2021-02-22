# The program:
# Your program must output the binary representation of each number given as input.
# Each number will be given on a separate line, you must output the binary result followed by a newline character in the same order.
# The binary representation must always start with a 1, except for the number 0 (no zero-padding).
#
# INPUT:
# Line 1: N, an integer for the amount of numbers to test.
# N next lines: X, an integer.
#
# OUTPUT:
# N lines: The binary representation of X.
#
# CONSTRAINTS:
# 0 < N ≤ 100
# 0 ≤ X ≤ 1000
#
# EXAMPLE:
# Input
# 6
# 0
# 1
# 2
# 3
# 9
# 256
# Output
# 0
# 1
# 10
# 11
# 1001
# 100000000

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n = int(input())
# for i in range(n):
#     x = int(input())
n=6
x=[6,0,1,2,3,9]

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario
for i in range(1,n):
    ou=binarizar(x[i])
# print("ones and zeros")
    print(ou)
# answer
# for i in'_'*int(input()):print(bin(int(input()))[2:])

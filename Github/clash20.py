# 	Goal
# You are given an N x N field which contains bombs 'b' and clear cells 'o'.
# Your task is to replace each clear cell with the number of bombs that it's surrounded and print the result.
# Input
# Line 1: An integer N, the size of matrix.
# Next N lines: Elements of the row separated by spaces( 'o' or 'b' ).
# Output
# N lines: Print the modified matrix.
# Constraints
# 2 ≤ N ≤ 20
# Example
# Input
# 4
# b o o b
# o o o o
# o b o o
# b o b o
# Output
# b 1 1 b
# 2 2 2 1
# 2 b 2 1
# b 3 b 1
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n = int(input())
# for i in range(n):
#     line = input()

n=4
b="b"
o="o"
line=[("b","o","o","b"),("o","o","o","o"),("o","b","o","o"),("b","o","b","o")]
# reemplace


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def bombs(a, i, j):
    k = 0
    for y in -1, 0, 1:
        for x in {-1, 1, int(y == 0)}:
            iy = i + y
            jx = j + x
            if 0 <= iy < len(a) and 0 <= jx < len(a[iy]):
                k += a[iy][jx] == 'b'
    return str(k)

n = int(input())
a = []
for i in range(n):
    s = input()
    a += [s.split()]
for i in range(n):
    for j in range(n):
        if a[i][j] == 'o':
            a[i][j] = bombs(a, i, j)
    print(*a[i])

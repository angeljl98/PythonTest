# The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
# 01 Test 1
# Input
# Expected output
# 5
# 5
# 5
# 5 5
# 5 10 5
# 5 15 15 5
# 5 20 30 20 5
# 02 Test 2
# Input
# Expected output
# 7
# 1
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
# 1 6 15 20 15 6 1
# 03 Test 3
# Input
# Expected output
# 3
# 10
# 10
# 10 10
# 10 20 10
# 04 Test 4
# Input
# Expected output
# 7
# 4276
# 4276
# 4276 4276
# 4276 8552 4276
# 4276 12828 12828 4276
# 4276 17104 25656 17104 4276
# 4276 21380 42760 42760 21380 4276
# 4276 25656 64140 85520 64140 25656

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# rows = int(input())
# s = [int(input())]

rows = int(5)
s = [int(5)]

print(*s)
for i in range(rows-1):
    a = [s[0]]
    for j in range(1,len(s)):
        a += [s[j]+s[j-1]]
    a += [s[-1]]
    print(*a)
    s=a

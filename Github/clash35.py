# Goal
# Give the ASCII representation of the hex encoded values
# Input
# Line 1: An integer N for the amount of values to decode
# Next N lines: An hex value C representing an ASCII character
# Output
# A single line containing the decoded ASCII characers.
# Constraints
# N < 100
# 00 ≤ C ≤ ff
# Example
# Input
# 11
# 68
# 65
# 6c
# 6c
# 6f
# 20
# 77
# 6f
# 72
# 6c
# 64
# Output
# hello world

n = int(input())
u=""
for i in range(n):
    c = input()
    u=u+(chr(int(c,16))) #convierte hexadecimal a decimal
print(u)

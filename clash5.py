# The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
# 01 Test 1
# Input
# Expected output
# Hello world
# eoo
# Hllwrld
# 02 Test 2
# Input
# Expected output
# empty
# ey
# mpt
# 03 Test 3
# Input
# Expected output
# Abcdefghihklmnopqrstuvwxyz
# Aeiouy
# bcdfghhklmnpqrstvwxz
# 04 Test 4
# Input
# Expected output
# Sort Values
# oaue
# SrtVls

#message = input()
message="Hello World"
vocales=("aeiouAEIOU")
m=""
o=""
for ct1 in vocales:
    for ct2 in message:
        if (ct2==ct1):
            m=m+ct2
for ct3 in message:
    cond1=True
    for ct4 in vocales:
        if (ct3==ct4):
            cond1=False
    if cond1==True:
        o=o+ct3
print(m)
print(o)

# opcional
# import sys
# import math
#
# # Auto-generated code below aims at helping you parse
# # the standard input according to the problem statement.
#
# message = input()
#
# # Write an answer using print
# # To debug: print("Debug messages...", file=sys.stderr, flush=True)
#
# s = 'aeiouyAEIOUY'
# print(''.join([x for x in message if x in s]))
# print(''.join([x for x in message if x not in s and  x != ' ']))


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

#print("answer")

# Goal
# A male ostrich weighs 20% more than a female one.
# Given the gender of an ostrich, and its weight, display the weight of its counterpart.
# If the gender is unknown, you should display "UNKNOWN".
# Input
# A single letter : 'F' for Female, 'M' for Male, any other char should be treated as unknown.
# An integer W representing the ostrich weight.
# Output
# The weight of the opposite gender ostrich truncated.
# Constraints
# 0 <= W < 200
# Example
# Input
# F
# 100
# Output
# 120

import sys
import math

g = input() #gender
w = int(input()) #weight

v=(str(w+20) if g=="F" else "")
v=(str(w-20) if g=="M" else v)
v=("UNKNOWN" if (g!="F" and g!="M") else v)
print(v)

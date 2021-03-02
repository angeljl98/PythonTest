# Goal
# In an Elementary School, the teacher is making all the students take turns in reading a story.
#
#
# This is done by assigning the students in a first to last list, then having each child read the next paragraph of the story. If every student has read, the order of students reading repeats from the beginning of the first to last list until the story is completely read.
#
# For Example, if the first to last list is of 3 students, (Jimmy Joan Jason) and the story is 5 paragraphs long, the reading session would go like:
# Jimmy - paragraph 1
# Joan - paragraph 2
# Jason - paragraph 3
# Jimmy - paragraph 4
# Joan - paragraph 5
#
#
# Your AIM is to find the child who would read the last paragraph of the story (last child reading) by name (Therefore your sample answer would be "Joan")
# Input
# First line: N and P separated with a single space (' ')
# P is the number of paragraphs of the story that the teacher gave the class
# Second line: list of N names of children in the class in reading order (first to last). The names are separated with a single space (' ')
# Output
# The Name of the child who would read the last paragraph of the story
# Constraints
# 1 ≤ N ≤ 17
# 1 ≤ P ≤ 40
# Names have only common letters
# Max length for a name = 8 chars
# Names are unique
# Example
# Input
# 3 20
# Jimmy Joan Jason
# Output
# Joan

import sys
import math
a=[]
n, p = [int(i) for i in input().split()]
for name in input().split():
    b=a.append(name)
    pass
    rt=0
for j in range(0,p):
    o=a[rt]
    rt+=1
    if rt>=n:
        rt=0
print(o)

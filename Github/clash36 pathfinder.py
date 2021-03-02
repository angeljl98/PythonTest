# 	Goal
# Pathfinding in 15 minutes! Can you do it? ...
#
# The Rules are simple:
# 1. There are N NODES number from 0 to N-1
# 2. There are L LINKS connecting the nodes
# 3. Each link is described as N1 - N2, meaning:
# (i) - You can go from N1 to N2,
# (ii) - You can also go from N2 to N1
# 4. You will be given the STARTING point S and ENDING point E
#
# You have To:
# Display minimum TIME to reach E from S
#
# Best of Luck! The clock is ticking...
# Input
# Line 1: An integer N, the number of nodes
# Line 2: An integer L, the number of links
# Next L lines: 2 integers N1 and N2, the 2 nodes of a link
# Next Line: 2 integers S and E, the starting and ending points
# Output
# Line 1: An integer T, the minimum time taken to reach E from S
# Constraints
# Example
# Input
# 4
# 4
# 0 1
# 0 2
# 1 3
# 2 3
# 0
# 3
# Output
# 2
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
l = int(input())
G = [1e5]*n
d = set()
for i in range(l):
    n1, n2 = [int(j) for j in input().split()]
    d|={(n1, n2), (n2, n1)}
s = int(input())
e = int(input())
G[s] = 0
for _ in range(n):
    for a, b in d:G[a]=min(1+G[b],G[a])
print(G[e])

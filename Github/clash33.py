# The program:
# Your program must reverse the positions of each word in the sentence given as input.
#
# INPUT:
# S, a string.
#
# OUTPUT:
# A string containing all the space-separated words of S in reverse order.
#
# CONSTRAINTS:
# S contains at least one word.
# S contains less than 1000 characters.
#
# EXAMPLE:
# Input
# Hello World
# Output
# World Hello

s = input()
v=s.split()
n=len(v)
t=""
for i in range(1,n+1):
    t=t+v[n-i]+" "
u=len(t)
print(t[0:(u-1)])

#mas corto
t = s.split()
print(' '.join(reversed(t)))

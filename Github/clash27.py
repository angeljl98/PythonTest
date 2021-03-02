# The program:
# Swap each character at an even position with the next character if there is one. Positions start at zero.
# INPUT:
# A single string s.
#
# OUTPUT:
# The transformed string.
#
# CONSTRAINTS:
# s contains less than 8192 characters.
#
# EXAMPLE:
# Input
# ABCDEF
# Output
# BADCFE

s = input()
n=len(s)
u=""
c=1
for i in range(1,n):
    if i%2==1:
        u=u+s[i]
        u=u+s[i-1]
if (n%2!=0):
    u=u+s[n-1]
print(u)

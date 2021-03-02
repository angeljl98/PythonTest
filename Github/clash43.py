

import math
w, h = [int(i) for i in input().split()]
x=y=0
for i in range(h):
    line = input()
    for j,c in enumerate(line):
        if c in 'AB':
            x+=[-j,j][x!=0]
            y+=[-i,i][y!=0]
print(round(math.hypot(x, y)))

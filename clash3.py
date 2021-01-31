# // You must output the percentage of points that are within the circle.
# //
# // A point on the edge of the circle is considered as inside of it.
# //
# // Input
# // Line 1: cx - Two space separated integers cx and cy for the coordinates of the circle center point
# // Line 2: r - Integer for the circle radius
# // Line 3: n - Integer for the number of points
# // Next n lines: Two space separated integers px and py for the coordinates of a point
# // Output
# // The percentage of points that are within the circle
# // Constraints
# // The testcases are designed in a way that the result will always be an integer in range 0 - 100
# // Example
# // Input
# // 5 4
# // 2
# // 1
# // 6 3
# // Output
# // 100
import math

n=4
points=[(5,4),2,1,(6,3)]
def solution(n,arg):
    cxy=arg[0]
    cx=cxy[0]
    cy=cxy[1]
    r=arg[1]
    n=arg[2]
    pxy=arg[3]
    px=pxy[0]
    py=pxy[1]
    percent=0
    for ct1 in range(0,n):
        d=math.sqrt(pow(cx-px,2)+pow(cy-py,2))
        if pow(d,2)<=pow(r,2):
            percent+=1
            print(percent)
    m=(percent*100)/n
    return m

var=solution(n,points)

print(var)

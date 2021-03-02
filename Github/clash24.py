# A man wants to rent an apartment in the city center. This man earns a euros per hour. Consider that he works for 6 hours per day for 5 days every week for four weeks. The apartment costs b euros per four weeks. You must also assume that you must consider spending c euros every four weeks for other reasons. It is necessary to produce "true" if he can afford the apartment or "false" if he can not.
#
# In fact, it is pretty easy!
# Good luck...
# Input
# Line 1: An integer a euro of profit per hour.
# Line 2: An integer b the cost of the apartment per four weeks.
# Line 3: An integer c other spending.
# Output
# Line 1: A string "true" or "false" if he can or cannot afford the apartment.
# Constraints
# Example
# Input
# 42
# 1200
# 1400
# Output
# true
# Console output
# N/A
# angeljl98
# Clashing...
# N/A
# Angelburgie22
# Clashing...
# N/A
# LannertvSeveir

import sys
import math
a = int(input()) #gana por hora
b = int(input()) #apartamento
c = int(input()) #cuanto gasta al mes semana
d=6*5*4 #cuantas horas trabaja al mes
if ((a*d)>(b+c)):
    print("true")
else:
    print("false")

print("true" if (a*120)>=(b+c) else "false") #resumen

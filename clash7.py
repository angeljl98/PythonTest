# You must automate a search bar for your browser software. If the user's input contains a dot "." then it's a www site and you redirect it to http://input
# Else, redirect to ftp://input
#
# If the input already contains http://, ftp:// or https:// do not redirect to anything else.

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# urlbar = input()
urlbar="www.google.com"
puntos=urlbar.count(".")

if puntos>0:
    newurlbar="http://"+urlbar
else:
    newurlbar="ftp://"+urlbar
alm1=urlbar.count("http://")
alm2=urlbar.count("ftp://")
alm3=urlbar.count("https://")
if alm1>0 or alm2>0 or alm3>0:
    newurlbar=urlbar

print(newurlbar)

# b=input()
b=urlbar
if b[:6]not in('ftp://','http:/','https:'):b=['f','ht']['.'in b]+'tp://'+b
print(b)

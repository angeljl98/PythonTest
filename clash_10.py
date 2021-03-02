# The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
# 01 Test 1
# Input
# Expected output
# 1
# 1
# 02 Test 2
# Input
# Expected output
# 2
# 2
# 22
# 03 Test 3
# Input
# Expected output
# 5
# 5
# 55
# 555
# 5555
# 55555
# 04 Test 4
# Input
# Expected output
# 6
# 6
# 66
# 666
# 6666
# 66666
# 666666
# 05 Test 5
# Input
# Expected output
# 9
# 9
# 99
# 999
# 9999
# 99999
# 999999
# 9999999
# 99999999
# 999999999
# n = int(input())
n=8
for i in range(1, n+1):
    print(str(n)*i)

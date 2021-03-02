# The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
# 01 Test 1
# Input
# Expected output
# This is SOO easy :loud_laugh:
# This is SOO easy XD
# 02 Test 2
# Input
# Expected output
# :) I am a CodinGamer :slight_smile:
# :) I am a CodinGamer :)
# 03 Test 3
# Input
# Expected output
# CoC is VERY good. Kinda obvious :stuck_out_tongue:
# CoC is VERY good. Kinda obvious :p
# 04 Test 4
# Input
# Expected output
# ChampionCoder is me :loud_laugh:
# ChampionCoder is me XD
# 05 Test 5
# Input
# Expected output
# Bit Hard: Can trip you up:):(XD:p:o
# Bit Hard: Can trip you up:):(XD:p:o
# 06 Test 6
# Input
# Expected output
# :open_mouth: :slight_smile: :disappointed: :loud_laugh: :stuck_out_tongue:
# :o :) :( XD :p
# Console output
# 100%
# 1015634
# Python3
# 100%
# BSoD
# Python3
# N/A
# D3t3erminat0r
# Java
# Pending...
# N/A
# CodeToJoy
# Python3
# Pending...
# N/A
# angeljl98
# Python3
# Pending...
# Standard Output S

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
new=s.replace(":loud_laugh:","XD")
new=new.replace(":slight_smile:",":)")
new=new.replace(":stuck_out_tongue:",":p")
new=new.replace(":open_mouth:",":o")
new=new.replace(":disappointed:",":(")

ou=""
for ct in new:
    ou=ou+str(ct)
print(ou)

# print(input().replace(':loud_laugh:', 'XD').replace(':slight_smile:', ':)').replace(':stuck_out_tongue:', ':p').replace(':open_mouth:', ':o').replace(':disappointed:', ':('))

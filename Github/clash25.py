# Your friend Alice wants to play the piano but finds it difficult to learn chords. So you decided to write a tool that will help her to practice.
#
# Your script should take a notes series notes and transpose it by semitones. It means moving all the notes up (or down for negative semitones) the same number of semitones (keys). A keyboard consists of notes:
# C C# D D# E F F# G G# A A# B
# and they are cycled, so after a 'B' it's a 'C' again and so on.
# Input
# Line 1 : A string notes with notes separated by spaces.
# Line 2 : An integer semitones showing the number of keys to move.
# Output
# A single line containing a transposed notes series. Notes are separated by spaces.
# Constraints
# notes can have from 1 to 3 notes.
# -48 <= semitones <= 48
# Example
# Input
# C E
# 1
# Output
# C# F
# Console output
# N/A
# shuo502
# Clashing...
# N/A
# StepBack13
# Clashing...
# N/A
# Scoopulanang
# Clashing...
# N/A
# angeljl98
# Clashing...
# N/A
# MohamedAbdallah
# Clashing...
# N/A
# thainameaw
# Clashing...

A='C C# D D# E F F# G G# A A# B'.split()
n=input().split()
s=int(input())
W=[]
for i in n:
    W.append(A[(A.index(i)+s)%12])
print(' '.join(W))

# You are given a list of lowercase words. Find how many words show up in the list more than once.
# Input
# Line 1: An integer N for the number of words in the list.
# Line 2: The list of words separated by a space.
# Output
# Line 1: Number of repeated words.
# Constraints
# Each word contains only lower-case letters.
# 1 ≤ N ≤ 10
# 1 ≤ length of a word ≤ 10
# Example
# Input
# 2
# different words
# Output
# 0
# Console output
# 100%
# ja_fica
# Code size: 65
# Python3
# 100%
# Tychkorg
# Code size: 355
# Python3
# 100%
# BitWolf
# Code size: 368
# Javascript
# N/A
# angeljl98
# Python3
# Pending...
# N/A
# RaviYadav123
# Java
# Pending...
# Standard Output Stream:
# 0
input()
s=input().split()
print(sum(s.count(i)>1for i in set(s)))

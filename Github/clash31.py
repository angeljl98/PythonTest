# Goal
# Given a word and a list of guesses, print out the hangman and Won if it was solved in time or Lost if the game was lost.
# Input
# First Line: word for the puzzle
# Second Line: Number of guesses taken n
# Next n Lines: Single valid character guess
# Output
# 3 Lines: A 3x3 partial or full hangman (including spaces)
# Possible Outputs in order (HINT: Just copy-paste if needed):
#     0  0  0  0  0  0
#        | /| /|\/|\/|\
#                /  / \
#
# 4th Line: Won or Lost depending on game result
# Constraints
# 6 incorrect guesses is a loss (full hangman)
# Completing the word before 6 incorrect guesses is a win
# 0 < len(word) <= 35
# word is all lowercase alphabet characters (no spaces or symbols)
# 0 < n <= 50
# All guesses are valid lowercase alphabet characters without repetition
# All games end after winning or losing
# All games are either won or lost
st1="    0  0  0  0  0  0 "
st2="       | /| /|\/|\/|\"
st3="               /  / \"
st4="Won"
st5="Lost"
ct=0
word = input()
n = int(input())
for i in range(n):
    guess = input()
    if word.find(guess)!=-1:
        ct+=1
    if ct>7:
        break
    if

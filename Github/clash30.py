# Goal
# Win "Rock Paper Scissors" against an unexperienced player!
#
# ROCK > SCISSORS
# PAPER > ROCK
# SCISSORS > PAPER
#
# In general a player, who has won one round of rock paper scissors, is going to use the same draw again
# and a person, who has lost, is going to change his draw to the draw, which beats the previous draw of the opponent.
# If there is a tie, then the player is going to act as he wins.
#
# Output the expected draw of your opponent and your own draw to win.
# Input
# A string S, which holds the opponent 's draw and your draw separated by a space of one round rock paper scissors.
# Output
# Output the expected next draw of your opponent and your draw to win the next round separated by a space.
# If the input contains an invalid draw, return "CHEATER"!
# Constraints
# Example
# Input
# ROCK PAPER
# Output
# SCISSORS ROCK

opponent, me = input().split()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

if opponent == 'ROCK':
    if me == 'ROCK':
        print('ROCK PAPER')
    elif me == 'PAPER':
        print('SCISSORS ROCK')
    elif me == 'SCISSORS':
        print('ROCK PAPER')
    else:
        print('CHEATER')
elif opponent == 'PAPER':
    if me == 'ROCK':
        print('PAPER SCISSORS')
    elif me == 'PAPER':
        print('PAPER SCISSORS')
    elif me == 'SCISSORS':
        print('ROCK PAPER')
    else:
        print('CHEATER')
elif opponent == 'SCISSORS':
    if me == 'ROCK':
        print('PAPER SCISSORS')
    elif me == 'PAPER':
        print('SCISSORS ROCK')
    elif me == 'SCISSORS':
        print('PAPER SCISSORS')
    else:
        print('CHEATER')
else:
    print('CHEATER')

# Once per race you may substitute your desired thrust with the keyword BOOST to grant your pod a burst of speed.
#
# Use the command <x y "BOOST"> instead of <x y power>.
#
#  	The Goal
# Win the race.
#  	Rules
# The circuit of the race is made up of checkpoints. To complete one lap, your vehicle (pod) must pass through each checkpoints in order and back through the start. The first player to reach the starting checkpoint on the final lap wins.
#
# The pods work as follows:
# To pass a checkpoint, the center of a pod must be inside the radius of the checkpoint.
# To move a pod, you must print a target destination point followed by a thrust value. Details of the protocol can be found further down.
# The thrust value of a pod is its acceleration and must be between 0 and 100.
# You can use 1 acceleration boost in the race, you need only replace the thrust value by the BOOST keyword.
#
# Victory Conditions
# Be the first to complete all the laps of the circuit with your pod.
#
# Lose Conditions
# Your program provides incorrect output.
# Your program times out.
# Your pod does not reach the next checkpoint in time.
# Somebody else wins.
#  	Expert Rules
# The game is played on a map 16000 units wide and 9000 units high. The coordinate X=0, Y=0 is the top left pixel.
#
# The checkpoints work as follows:
# The checkpoints are circular, with a radius of 600 units.
# The disposition of the checkpoints is selected randomly for each race.
# The pods work as follows:
# If none of your pods make it to their next checkpoint in under 100 turns, you are eliminated and lose the game.
# The pods may move normally outside the game area.
#
# Note: You may activate debug mode in the settings panel () to view additional game data.
#  	Note
# The program must, within an infinite loop, read the contextual data from the standard input and provide to the standard output the desired instructions.

import sys
import math
import random

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

tiempo = 0

# game loop
while True:
    tiempo+=1
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]
    inc_x=1000
    inc_y=0
    min=random.randrange(0, 50)
    if x<next_checkpoint_x and min>10:
        inc_x=-500
    else:
        inc_x=500
    if y<next_checkpoint_y and min>10:
        inc_y=-500
    else:
        inc_y=500

    next_checkpoint_x=next_checkpoint_x+inc_x
    next_checkpoint_y=next_checkpoint_y+inc_y
    d1=((x-next_checkpoint_x)**2+(x-next_checkpoint_y)**2)**0.5
    d2=next_checkpoint_dist
    min=random.randrange(50, 100)
    if (next_checkpoint_angle>70 or next_checkpoint_angle<-70):
        rel_val=min
    else:
        rel_val=int(100*(d1/d2))

    if (rel_val>100):
        pct_val=100
    elif (rel_val<0):
        pct_val=0
    else:
        pct_val=rel_val
    # Convert thrust
    dado=random.randrange(0, 100)
    if d1>5000 and (next_checkpoint_angle==0) and dado >50:
        thrust=" BOOST"
    else:
        thrust=" "+str(pct_val)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + thrust)

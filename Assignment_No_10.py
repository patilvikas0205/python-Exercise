'''
10. A robot moves in a plane starting from the original point (0,0). The robot
can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2

The numbers after the direction are steps.
Please write a program to compute the distance from current position
after a sequence of movement and original point.
If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2 (Use euclidean distance formula )

'''

import math
x,y=0,0

while True:
    moves=input("Enter Moves of Robot UP/DOWN/LEFT/RIGHT if want to Stop pls enter STOP: ")

    if moves=='STOP':
        break

    else:
        #moves=tuple(moves)
        moves=moves.split()
        #print(type(moves))
        #print(moves)

    if moves[0]=='UP':
        x=x+int(moves[1])

    if moves[0]=='DOWN':
        x=x-int(moves[1])

    if moves[0]=='RIGHT':
        y=y+int(moves[1])

    if moves[0]=='LEFT':
        y=y-int(moves[1])

Current_position=math.sqrt(x**2-y**2)
print("Current Postionof Robot is: ",math.ceil(Current_position))


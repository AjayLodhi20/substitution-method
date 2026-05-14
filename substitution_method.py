# 1. take values for an equation
# 1a. add + -
# 2. take those values and turn it into x and y and any alphabet and constant on right hand sides
# 2a. isolate x or y
# 3. put that x or y in second equation and solve it
# 4. write the formula to solve by putting the value - diff for diff no of eq
# 5. what if there are more than three equations - allow till three equations
# 6. use +,-,*,/
# 7. return a tuple with x and y coordinates
import random
from operator import add, mul, sub

# 1. take values for an equation
class Equation:
    OPS = {
        '+' : add,
        '-' : sub,
    }


    def values(self):
        a = int(input("Enter Co-efficient for x: "))
        s = int(input("Enter sign + or -"))
        b = int(input("Enter Co-efficient for y: "))
        c = int(input('Enter constant: '))


    # def __init__(self):
    #
    # def __str__(self):
    #     return f"{}x"

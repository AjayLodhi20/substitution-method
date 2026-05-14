# 1. take values for an equation
# 2. take those values and turn it into x and y and any alphabet and constant on right hand sides
# 2a. isolate x or y
# 3. put that x or y in second equation and solve it
# 4. write the formula to solve by putting the value - diff for diff no of eq
# 5. what if there are more than three equations - allow till three equations
# 6. use +,-,*,/
# 7. return a tuple with x and y coordinates


# 1. take values for an equation
class Equation:
    def __init__(self, x=0, y=0, z=0, cons=0):
        self.x = x
        self.y = y
        self.z = z
        self.cons = cons
        

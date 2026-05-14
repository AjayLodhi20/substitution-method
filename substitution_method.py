# 1. take values for an equation
# 1a. add + -
# 2. take those values and turn it into x and y and any alphabet and constant on right hand sides
# 2a. isolate x or y
# 3. put that x or y in second equation and solve it
# 4. write the formula to solve by putting the value - diff for diff no of eq
# 5. what if there are more than three equations - allow till three equations
# 6. use +,-,*,/
# 7. return a tuple with x and y coordinates

import operator as op
# 1. take values for an equation
class Equation:
    def __init__(self,sign_func, x=1, y=1, c=0):
        self.a = x
        self.sign = self.operators(sign_func)
        self.b = y
        self.c = c
# 1a. add + -

    def operators(self, sign):
        if sign ==  '+' :
            return  op.add
        return  op.sub

    def first(self):
        if self.a == 0:
            return 'undefined'
        if self.sign == op.add:
            x = (self.c - self.b)/self.a
            return x
        else:
            x = (self.c + self.b)/self.a
            return x

    def finding_2nd(self):


eq1 = Equation('+', 2, 2, 2 )

print(eq1.first())

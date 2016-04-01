import scipy.integrate as integrate 
import scipy.special as special 
import numpy as np

def make_lambda(n):
    if type(n) in [int, float]:
        return lambda: n

class tint():
    def __init__(self):
        self.outer_lower, self.outer_upper = (0,0)
        self.mid_lower, self.mid_upper = (0,0) # Stop being lazy
        self.inner_lower, self.inner_upper = (0,0)
        self.density = 1
        print(self.outer_lower, self.mid_upper, self.inner_lower, self.density)

    def tintt(function):
        return integrate.tplquad(function,\
                                self.outer_lower, self.outer_upper,\
                                 make_lambda(self.mid_lower), make_lambda(self.mid_upper),\
                                 make_lambda(self.inner_upper), make_lambda(self.inner_upper))

    # default something...rho
# SHIFT-K gives help page from vim

newTint = tint()
this_list = [lambda outer: outer, lambda outer,mid: 1 + outer + mid, 1]
newTint.outer_upper = this_list[2]
newTint.mid_upper = this_list[1]
newTint.inner_upper = this_list[0]

print (newTint.tintt(lambda: 1))

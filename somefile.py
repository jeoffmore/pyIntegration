import scipy.integrate as integrate
import scipy.special as special
import numpy as np
def f(x,y,z):
    return 8*x*y*z

def bounds_z():
    return [0,1]

def bounds_y():
    return [2,3]

def bounds_x():
    return [1,2]

print (integrate.nquad(f, [bounds_z(), bounds_x(), bounds_y()]))
# ^^ Expects 15 ^^ 
f = lambda x: np.exp(-x)*np.sin(x)
l = integrate.quad(f,0,2*np.pi)
print(l)

def func(x,y,z):
    return 1

def this_is(n):
    return n
# tplquad expects x to have constants

hit_the_quad = integrate.tplquad(func(1,1,1),\
                                 0, 1,\
                                 lambda x: x, lambda x: 1-2*x,\
                                 lambda: 0, lambda x, y: 1+x+y) # May need space after each var
print(hit_the_quad)
# No idea why above gives "<lambda>() takes 0 positional arguments but 2 were given error"

def test_triple_integral():
    # 9) Triple Integral test
    def simpfunc(z, y, x):      # Note order of arguments.
            return x+y+z
 
            a, b = 1.0, 2.0
            tplquad(simpfunc, a, b,\
                    lambda x: x, lambda x: 2*x,\
                    lambda x, y: x - y, lambda x, y: x + y)

print(test_triple_integral())

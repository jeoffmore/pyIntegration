from scipy import integrate

def f(x,y):
    return x*y # Maybe default return to 1 for triple integration(cartesian)

def bounds_y(): # args are what function is in terms of
    return [0, 0.5]

def bounds_x(y):
    return [0, 1-2*y]

area = integrate.nquad(f, [bounds_x, bounds_y]) # Inner to outer with nquad
# possibly assume x,y,z are all 1 unless specified for class function
# lambda 1*
# [1,1]
# needs to eval to 1 for integral of z portion. Stop guessing
print(area)


def g(o, m, i): # outer, middle, inner
    return 1 # default 1

def bounds_o():
    return [0, 1]
def bounds_m(o):
    return [0, 2*(1-o)]
def bounds_i(o,m):
    return [0, 3*((1-m)/(2-o))]

tArea = integrate.nquad(g, [bounds_i, bounds_m, bounds_o])
print(tArea)
"""nquad is definately easier for simple integrals
perhaps it could be further simplified by wrapping a class around bounds o, m, i
I probably still should learn how to use tplquad.."""

""" Centre of Mass """
# integral w respecitve dimension divided by mass
rho = 3 # or some funct
# new g = lambda a, b: g(x,y,z) * rho(x,y,z)
vol = integrate.nquad(g, [bounds_i, bounds_m, bounds_o])
print(vol)

def h(o, m, i):
    return 1
def rho(o,m,i):
    return 3

herho = lambda o, m, i: h(o,m,i) * rho(o,m,i)
mass2 = integrate.nquad(herho, [bounds_i, bounds_m, bounds_o])
print(mass2)
# Now rho and h can be functions and live appily ever after

#Now I have to calculate centre of mass
def com(mass): # must corespond with variables used for integration
    lol = integrate.nquad(lambda o,m,i: h(o,m,i) * o,\
                          [bounds_i, bounds_m, bounds_o])
    lml = integrade.nquad(lambda o,m,i: h(o,m,i) * m,\
                          [bounds_i, bounds_m, bounds_o])
    lil = integrade.nquad(lambda o,m,i: h(o,m,i) * i,\
                          [bounds_i, bounds_m, bounds_o])

    return lol/mass2, lml/mass2, lil/mass2

print(com(mass2))


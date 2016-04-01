from scipy import integrate


def bounds_o():
    return [0, 1]
def bounds_m(o):
    return [0, 2-o] # original upper bound: 2(1-o)
def bounds_i(o,m):
    return [0, 3*((1-m)/(2-o))]

def h(o, m, i):
    return 1
def rho(o,m,i):
    return 3

herho = lambda o, m, i: h(o,m,i) * rho(o,m,i)
mass2 = integrate.nquad(herho, [bounds_i, bounds_m, bounds_o])
print(mass2)
# Now rho and h can be functions and live appily ever after

#Now I have to calculate centre of mass
lol = integrate.nquad(lambda o,m,i: i * h(o,m,i),\
                      [bounds_i, bounds_m, bounds_o])
"""lol = integrate.nquad(lambda o,m,i: h(o,m,i) * o,\
                      [bounds_i, bounds_m, bounds_o])"""


print(lol)


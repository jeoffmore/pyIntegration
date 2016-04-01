from scipy import integrate

def integrand(x, a, b):
    return a * x + b

a = 2
b = 1
I = integrate.quad(integrand, 0, 1, args=(a,b))
print(I)

area = integrate.dblquad(lambda x,y: x*y,\
                       0, 0.5,\
                       lambda x: 0, lambda x: 1-2*x)
print(area)

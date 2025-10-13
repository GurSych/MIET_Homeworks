import sympy as sp

x = sp.Symbol('x')
f = sp.tan(x**2)-sp.sin(x**2)
a = sp.limit(f/x**6,x,0)
print(a)

def range(start,end,step):
    while(start < end):
        start += step; yield start

for r in range(.1,10,.1):
    a = sp.limit(f/x**r,x,0)
    if a not in (-sp.oo, 0, sp.oo):
        print(f'{a}, r = {r}')
import sympy as sp

x = sp.Symbol('x')
f = ((x**2)-1)*sp.ln(x)
a = sp.limit(f/x**-.00000000000000000000000000000000000000000000000000000001,x,0)
print(a)

def range(start,end,step):
    while(start < end):
        start += step; yield start

for r in range(-.0002,.0002,.00001):
    a = sp.limit(f/x**r,x,0)
    #if a not in (-sp.oo, 0, sp.oo):
    print(f'{a}, r = {r}')
import sympy as sp

x = sp.Symbol('x')
from sympy.parsing.sympy_parser import parse_expr

y = parse_expr(input("Enter equation in terms of x: "))

print('slope:', float(y.coeff(x)))
print('y_intercept:', float(y.subs(x, 0)))
print('x_intercept:', (float(y.subs(x, 0))*-1)/(float(y.coeff(x))))

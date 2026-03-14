import sympy as sp

A = sp.Matrix([
    [sp.sqrt(3)/2, sp.sqrt(3)/2],
    [sp.Rational(1, 2),      -sp.Rational(1, 2)]
])

print("A =")
sp.pprint(A)

print("\nA^6 =")
sp.pprint(A**6)

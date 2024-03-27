from sympy import symbols, Eq, solve

a, b, c, d, e = symbols('a b c d e')

equations = [
    Eq(a - b + c + d - e, 195),
    Eq(a + b - c - d + e, 49),
    Eq(a - b - c + d + e, 223),
    Eq(a + b + c - d - e, 21),
    Eq(a - b + c - d + e, 173),
    Eq(a + b - c + d - e, 71),
    Eq(a - b - c - d - e, -231),
    Eq(a + b + c + d + e, 475)
]

solution = solve(equations, (a, b, c, d, e))
print(solution)

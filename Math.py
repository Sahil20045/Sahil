import math

def solve_quadratic(a, b, c):
    if a == 0:
        if b == 0:
            return "No solution, both 'a' and 'b' are zero."
        return f"Linear solution: x = {-c / b}"
    
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"Two distinct real roots: x1 = {root1}, x2 = {root2}"
    elif discriminant == 0:
        root = -b / (2 * a)
        return f"One real root (double root): x = {root}"
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        return f"Two complex roots: x1 = {real_part} + {imaginary_part}i, x2 = {real_part} - {imaginary_part}i"


a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

result = solve_quadratic(a, b, c)
print(result)

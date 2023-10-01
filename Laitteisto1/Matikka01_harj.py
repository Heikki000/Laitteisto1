import sympy as sp

# Define symbolic variable
j = sp.symbols('j')

# Define the matrix eee
eee = sp.Matrix([[1 - 1j, -1j], [1j, 1 - 1j]])

# Calculate the determinant symbolically
determinant = eee.det()

# Simplify the result
simplified_determinant = sp.simplify(determinant)

print(simplified_determinant)
#Laitteisto1 / Matikka4, tehtava 2
from sympy import symbols, solve
x, y, z, a, b, c = symbols('x, y, z, a, b, c')

#tehtava 1 a)
answer_1a = solve([x - 2*y - 2*z, -2*x + y - z + 3, 3*x + 2*y + z - 4], [x, y, z])
print(answer_1a)

#tehtava 1 b)
answer_1b = solve([x + y - 1, 2*x + y - z - 1, 3*x + y - 2*z - 1], [x, y, z])
print(answer_1b)

#tehtava 2 a)
answer_2a = solve([2*x + 4*y - z - 11, 6*x - y - 3*z - 7, 4*x + 5*y - 2*z - 16], [x, y, z])
print(answer_2a)

#tehtava 2 b)
answer_2b = solve([4*x + 2*y - 2*z, 2*x + y - z - 1, 3*x + y - 2*z - 1], [x, y, z])
print(answer_2b)

#matikka2 kertaustahtava
kertaus_1a = solve([5*x + 3*y - 9, 2*x + y - 4], [x, y])
kertaus_1b = solve([2*x + y + z - 6, x + 3*y + z - 2, 2*x + y + 2*z - 9], [x, y, z])
kertaus_1c = solve([x + z + 3*z + 1, 3*x + y + z - 5, 2*x + y + 2*z - 2], [x, y, z])
print(kertaus_1a)
print(kertaus_1b)
print(kertaus_1c)

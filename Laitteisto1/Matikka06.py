#Laitteisto1 / Matikka6
import numpy as np
import numpy.linalg as la
#   Käänteismatriisi lasketaan Pythonissa komennolla numpy.linalg.inv().
# MINVERSE-komento excelissä tekee käänteismatriisin
# MDETERM-komento laskee determinantin
# MMULT kertoo keskenään
a = np.array([[2, 0, 0], [1, 3, 0], [5, 4, 1]])
b = np.array([[5, 1, 2], [1, 4, 2], [2, 2, 2]])
a_2 = np.array([[4, 5], [3, 7]])
b_2 = np.array([[5, 10], [-8, 6]])

aa = la.inv(a)
bb = la.inv(b)
aa_b = la.inv(a_2)
bb_2 = la.inv(b_2)

print(aa)
print(bb)
print(aa_b)
print(bb_2)
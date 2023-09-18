#Laitteisto1 / Matikka5, tehtava 4
import numpy as np
#tehtava 1
#a)
yksi_a = np.array([[-1, 2], [3, 1]])
yksi_b = np.array([[0, 1, 3], [2, -3, 5]])
print(np.dot(yksi_a, yksi_b))

#b)

yksi_aa = np.array([[1, 3, 5], [0, -2, 1], [2, -1, 4]])
yksi_bb = np.array([[1], [-3], [-1]])
print(np.dot(yksi_aa, yksi_bb))

#c)

yksi_aaa = np.array([[2, 0, 1], [1, -3, 4], [0, 1, 5]])
ysi_bbb = np.array([[3], [-5], [7]])
print(np.dot(yksi_aaa, yksi_bbb))

#d)

yksi_aaaa = np.array([[1, -4, 2], [3, 0, -2], [2, 1, 0]])
yksi_bbbb = np.array([[5, 1, -1], [-2, 1, 3], [0, 3, 4]])
print(np.dot(yksi_aaaa, yksi_bbbb))
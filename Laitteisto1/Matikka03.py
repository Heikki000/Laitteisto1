#Laitteisto1 / Matikka, tehtava 4
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

#teht. 1
aa = np.array([[-1, 2], [3, -5]])
bb = np.array([[2, 0], [-1, 4]])
print(2*aa+3*bb)
print(aa-bb)

#teht. 2
aaa = np.array([[1+1j, 3, 1j], [0, 5+1j, 1j]])
ccc = (1+1j) * aaa
print(ccc)

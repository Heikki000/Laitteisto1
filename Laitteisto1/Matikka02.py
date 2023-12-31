#Laitteisto1 / Matikka, tehtava 2
import numpy as np
#1
lukutaulukko = np.array([1, 5, 11, 18, 100])
print(f"Tehtävän 1 lukutaulukko on {lukutaulukko}.")
'''
print("lukutaulukko -> ndim:", lukutaulukko.ndim)
print("lukutaulukko -> shape:", lukutaulukko.shape)
print("lukutaulukko -> size:", lukutaulukko.size)
print("lukutaulukko -> dtype:", lukutaulukko.dtype)
'''
#2
u = np.array([2, 3])
v = np.array([4, -7])
uu = np.array([1, 1, 1])
vv = np.array([3, -3, 2])
print(f"Tehtävän 2 vektorit ovat {u}, {v}, {uu} sekä {vv}.")

#3
norm_u = np.linalg.norm(u)
norm_v = np.linalg.norm(v)
norm_uu = np.linalg.norm(uu)
norm_vv = np.linalg.norm(vv)
print(f"Vektorien normit ovat {norm_u:.2f}, {norm_v:.2f}, {norm_uu:.2f} sekä {norm_vv:.2f}.")

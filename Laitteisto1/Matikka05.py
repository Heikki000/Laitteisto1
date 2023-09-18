#Laitteisto1 / Matikka5, tehtava 4
import numpy as np
import numpy.linalg as la
#tehtava 1
#a)
yksi_a = np.array([[-1, 2], [3, 1]])
yksi_b = np.array([[0, 1, 3], [2, -3, 5]])
tulo_a = np.dot(yksi_a, yksi_b)
print("Tehtava 1")
print(tulo_a)

#b)

yksi_aa = np.array([[1, 3, 5], [0, -2, 1], [2, -1, 4]])
yksi_bb = np.array([[1], [-3], [-1]])
tulo_aa = np.dot(yksi_aa, yksi_bb)
print(tulo_aa)


#c)

yksi_aaa = np.array([[2, 0, 1], [1, -3, 4], [0, 1, 5]])
yksi_bbb = np.array([[3], [-5], [7]])
tulo_aaa = np.dot(yksi_aaa, yksi_bbb)
print(tulo_aaa)

#d)

yksi_aaaa = np.array([[1, -4, 2], [3, 0, -2], [2, 1, 0]])
yksi_bbbb = np.array([[5, 1, -1], [-2, 1, 3], [0, 3, 4]])
tulo_aaaa = np.dot(yksi_aaaa, yksi_bbbb)
print(tulo_aaaa)

#tehtava 2
print()
print("Tehtava 2. transpoosit 1")
#transpoosit
#A
qq = np.array([4, 9, 0], [-3, 7, -11])
print(np.transpose(qq))
# print(tulo_a.T)       /toinen merkintätapa
#B
ww = np.array([[8, 9], [-3, 12], [0, -1], [7, 1]])
print(np.transpose(ww))
print()
print("Tehtava 2. determinantit 1")
#determinantit          /numpy.linalg.det()
print()
print("Tehtava 2. determinantit")
#a)
#print(la.det(tulo_a))      /ei voi laskea, koska ei ole neliömatriisi
#b)
#print(la.det(tulo_aa))      /ei voi laskea, koska ei ole neliömatriisi
#c)
#print(la.det(tulo_aaa))     /ei voi laskea, koska ei ole neliömatriisi
#d)
print(la.det(tulo_aaaa))
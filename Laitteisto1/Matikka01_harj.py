import numpy as np

# Määritellään matriisi A
A = np.array([[1+1j, 3j]])

# Määritellään kerrottava luku (1+i)
kerrottava_luku = 1 + 1j

# Suoritetaan kertolasku
tulos = kerrottava_luku * A

# Tulostetaan tulos
print("Tulos:")
print(tulos)
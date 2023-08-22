#tehtava 2
import math

vastaus_1a = math.degrees(2.493)
vastaus_1b = math.degrees(0.911)

vastaus_2a = math.radians(137.7)
vastaus_2b = math.radians(62.3)

taulukko_degree = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360]
sanakirja_radians = {}

for n in taulukko_degree:
    radiaani = math.radians(n)
    sanakirja_radians[n] = f"{radiaani:.2f}"

hypotenuusa = math.hypot(2.3, 4.7)
kulma_1 = math.degrees(math.atan(2.3/4.7))
kulma_2 = math.degrees(math.atan(4.7/2.3))

taulukko_number = [0, 4, 7, 15]
sanakirja_factorial = {}

for n in taulukko_number:
    factorial_n = math.factorial(n)
    sanakirja_factorial[n] = f"{factorial_n}"

print(vastaus_1a)
print(vastaus_1b)
print(vastaus_2a)
print(vastaus_2b)
print(sanakirja_radians)
print(f"Hypotenuusa on {hypotenuusa:.1f} ja 2 kulmaa ovat {kulma_1:.1f} ja {kulma_2:.1f}.")
for key, value in sanakirja_factorial.items():
    print(f"{key}! : {value}")



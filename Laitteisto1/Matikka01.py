"tehtava 2"
import math

vastaus_1a = math.degrees(2.493)
vastaus_1b = math.degrees(0.911)

vastaus_2a = math.radians(137.7)
vastaus_2b = math.radians(62.3)

taulukko_degree = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360]
taulukko_radians = []

for n in taulukko_degree:
    radiaani = math.radians(n)
    taulukko_radians.append(radiaani)

print(vastaus_1a)
print(vastaus_1b)
print(vastaus_2a)
print(vastaus_2b)
print(taulukko_radians)


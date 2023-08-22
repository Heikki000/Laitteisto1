import math

taulukko_degree = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360]
taulukko_radians = {}

for n in taulukko_degree:
    radiaani = math.radians(n)
    taulukko_radians[n] = f"{radiaani/180:.2f}π"

print(taulukko_radians)

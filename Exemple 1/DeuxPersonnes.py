import random
import math
nb_simul = 5000
SV = 0
for k in range(nb_simul):
    arr1 = random.randint(0, 60)
    arr2 = random.randint(0, 60)
    c = abs(arr1 - arr2)
    SV += c

MV = SV/nb_simul

print("Estimation ponctuelle", MV)

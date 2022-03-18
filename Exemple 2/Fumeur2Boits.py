import random
import math

SV = 0
nb_simul = 5000
for k in range(nb_simul):
    Boite1 = 40
    Boite2 = 40
    encore = True
    while encore:
        if random.random() < 0.5:
            Boite1 -= 1
        else:
            Boite2 -= 1
        if Boite1 == 0 or Boite2 == 0:
            encore = False
    r = Boite1+Boite2
    SV += r

MV = SV/nb_simul
print('Estimation ponctuele =', int(MV))

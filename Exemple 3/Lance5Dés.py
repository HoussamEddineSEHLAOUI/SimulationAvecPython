import random
import math

SV = 0
nb_simul = 5000
for k in range(nb_simul):
    des = 5
    lancers = 0
    encore = True
    while encore:
        for k in range(des):
            if random.randint(1, 6) == 1:
                des -= 1
        lancers += 1
        encore = (des != 0)
    SV = SV + lancers

MV = SV/nb_simul
print('Estimation ponctuele =', int(MV))

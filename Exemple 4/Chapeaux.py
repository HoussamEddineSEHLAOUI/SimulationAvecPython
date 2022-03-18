import random
import math
N = 50
somme = 0
nb_simul = 5000
for s in range(nb_simul):
    chapeaux = list(range(N))
    random.shuffle(chapeaux)
    for p in range(N):
        if chapeaux[p] == p:
            somme += 1
            break
MV = somme/nb_simul
print('Estimation ponctuele =', MV)

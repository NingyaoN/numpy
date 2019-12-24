height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

np_height = np.array(height)
np_weight = np.array(weight)

#print(type(np_height), type(np_weight))

#calculate bmi

#bmi1 = weight / height ** 2 WRONG
bmi = np_weight / np_height**2
#print(bmi)
#print(bmi1)

#   printing bmi greater than 25.
#   hard way.

for b in bmi:
    if b > 25:
        print(b)

#   using numpy
print(bmi[bmi > 25])

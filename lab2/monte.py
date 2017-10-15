# monte.py
# approximates pi using monte carlo method

import random
import math

def monte():

darts = int(input('you said you wanna throw HOW many darts at me? '))
hits = 0

for i in range(darts):
    rand_x = random.uniform(-1.0, 1.0)
    rand_y = random.uniform(-1.0, 1.0)
    if (math.sqrt(rand_x * rand_x + rand_y * rand_y) <= 1):
        hits += 1

monte()
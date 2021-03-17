##Timothy Young, CS350, Bottum-UP RodCutting Algorithm
##HW6

import numpy as np
import time
import random

def rodCut(n,P=[]):
    inf = np.NINF
    maxRev = [0,0,0,0,0]
    for j in range(0,n):
        q = inf
        for i in range(0,j):
            q = max(q,P[i] + maxRev[j-i])

        maxRev.append(q)
    return maxRev[-1]

P = [1,2,5,7,8,9,9,10,11,12]
n = 10
n2 = 100
n3 = 1000
n4 = 10000

P2 = []
for i in range(100):
    r = random.randint(1,12)
    P2.append(r)
P2.sort()

P3 = []
for i in range(1000):
    r = random.randint(1,12)
    P3.append(r)
P3.sort()

P4 = []
for i in range(10000):
    r = random.randint(1,12)
    P4.append(r)
P4.sort()

print("TestCase#1:")
t1 = time.perf_counter()
revenue = rodCut(n,P)
t2 = time.perf_counter()
totalTime = t2-t1
print("maxRevenue:", revenue, "Time",totalTime, "n = ", n)
print("_______________")


print("TestCase#2:")
t3 = time.perf_counter()
revenue2 = rodCut(n2,P2)
t4 = time.perf_counter()
totalTime2 = t4-t3
print("maxRevenue:", revenue2, "Time",totalTime2, "n = ", n2)
print("_______________")


print("TestCase#3:")
t5 = time.perf_counter()
revenue3 = rodCut(n3,P3)
t6 = time.perf_counter()
totalTime3 = t6-t5
print("maxRevenue:", revenue3, "Time",totalTime3, "n = ", n3)
print("_______________")


print("TestCase#4:")
t7 = time.perf_counter()
revenue4 = rodCut(n4,P4)
t8 = time.perf_counter()
totalTime4 = t8-t7
print("maxRevenue:", revenue4, "Time",totalTime4, "n = ", n4)
print("_______________")




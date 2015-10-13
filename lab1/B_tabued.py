from time import time

__author__ = 'dantipov'

from random import randint, random
from math import sqrt

def real_f(x):
    print("".join([str(x_i) + " " for x_i in x]))
    res = input()
    if res == 'Bingo':
        exit(0)
    else:
        return float(res)

def test_f(x):
    res = min(1 + 2 * (x[0] - 1) ** 2,
               2 + 1.8 * (x[0] - 2) ** 2,
               3 + 1.6 * (x[0] - 3) ** 2,
               4 + 1.4 * (x[0] - 4) ** 2,
               5 + 1.2 * (x[0] - 5) ** 2)
    if res < 1.001:
        print(x)
        print('Bingo')
        exit(0)
    return res + random() - 0.5

beta = [random() * 20 - 10 for i in range(5)]
gamma = [random() + 1 for i in range(5)]
alpha_rand = [[random() * 20 - 10 for i in range(5)] for j in range(10)]
calls = 0
def dim10_test_f(x):
    global calls
    calls += 1
    res = min([beta[i] + gamma[i]  * sum([(x[j] - alpha_rand[j][i]) ** 2  for j in range(10)]) for i in range(5)])
    if res < min(beta) + 0.001:
        print('Bingo')
        exit(0)
    return res + random() - 0.5

f = real_f



#tabued is a binary vector that shows, which mutations were already checked
def local_search(x):
    value = f(x)
    tabooed = [0] * (2 * len(x))
    tabooed_number = 0

    while (tabooed_number != len(x)):
        mutation = [i for i in range(len(tabooed)) if tabooed[i] < 1][randint(0, len(tabooed) - tabooed_number - 1)]
        x[mutation // 2] += 0.1 - 0.2 * (mutation % 2)
        if (abs(x[mutation // 2]) > 10):
            tabooed[mutation] = 1
            x[mutation // 2] += -0.1 + 0.2 * (mutation % 2)
            tabooed_number += 1
        new_value = f(x)
        if new_value > value:
            tabooed[mutation] = 1
            x[mutation // 2] += -0.1 + 0.2 * (mutation % 2)
            tabooed_number += 1
        else:
            tabooed = [0] * (len(x) * 2)
            tabooed[mutation + 1 - mutation % 2] = 1
            tabooed_number = 1
            value = new_value
    return x

#this are zones of local minimums
globally_tabooed = []

def dist(x, y):
    return sqrt(sum([(x[i] - y[i]) ** 2 for i in range(len(x))]))

def check_tabooed(x):
    global globally_tabooed
    for y in globally_tabooed:
        if dist(x, y) < 0.42:
            return True
    return False

n = int(input())
best = 100

while calls < 10000 * n ** 2:
    x = [random() * 20.0 - 10.0 for i in range(n)]
    if not check_tabooed(x):
        local_min = local_search(x)
        if not check_tabooed(local_min):
            globally_tabooed.append(local_min)

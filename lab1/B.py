
__author__ = 'Den'
 
from random import random, randint
from time import time
 
def real_f(x):
    str_x = ""
    for x_i in x:
        str_x += str(x_i) + " "
    print(str_x)
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
def dim10_test_f(x):
    res = min([beta[i] + gamma[i]  * sum([(x[j] - alpha_rand[j][i]) ** 2  for j in range(10)]) for i in range(5)])
    if res < min(beta) + 0.001:
        print('Bingo')
        exit(0)
    return res + random() - 0.5

 
f = dim10_test_f
 
 
 
n = int(input())
pop_size, iterations = 100 * n, 100 * n
 
alpha = 0.5
crossover = 0.2
pop = [[random() * 20 - 10 for i in range(n)] for j in range(pop_size)]
values = [f(x) for x in pop]
 
for iter in range(iterations):
    print(iter)
    # t = time()
    new_pop = []
    new_values = []
    # print(time() - t)
    for i in range(pop_size):
        t = time()
        a, b, c = randint(0, pop_size - 1), randint(0, pop_size - 2), randint(0, pop_size - 3)
        if b >= a: b += 1
        if c >= min(a, b): c += 1
        if c >= max(a, b): c += 1
        # print("random:", time() - t)
        # t = time()
        new_individual = [pop[a][i] + alpha * (pop[b][i] - pop[c][i]) for i in range(n)]
        # print("new_individual:", time() - t)
        # t = time()
        #crossover
        for j in range(n):
            if random() < crossover:
                new_individual[j] = pop[i][j]
        # print("crossover:", time() - t)
        # t = time()
        #we've got new candidate
        new_value = f(new_individual)
        if new_value < values[i]:
            new_values.append(new_value)
            new_pop.append(new_individual)
        else:
            new_values.append(values[i])
            new_pop.append(pop[i])
    # exit(0)
    values = new_values
    pop = new_pop
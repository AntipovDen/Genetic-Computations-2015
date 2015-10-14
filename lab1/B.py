from time import time

__author__ = 'Den'
 
from random import random, randint


this_is_the_end = False

def real_f(x):
    print("".join([str(x_i) + " " for x_i in x]))
    res = input()
    if res == 'Bingo':
        exit(0)
    else:
        return float(res)


def test_f(x):
    res = min(1. + 2. * (x[0] - 1) ** 2,
               2. + 1.8 * (x[0] - 2) ** 2,
               3. + 1.6 * (x[0] - 3) ** 2,
               4. + 1.4 * (x[0] - 4) ** 2,
               5. + 1.2 * (x[0] - 5) ** 2)
    if res < 2.001:
        print(x)
        print('Bingo')
        exit(0)
    return res + random() - 0.5

beta = [1., 2., 3., 4., 5.]
gamma = [2., 1.8, 1.6, 1.4, 1.2]
#gamma = [1., 1.2, 1.4, 1.6, 1.8]
alpha_rand = [[random() * 20. - 10. for i in range(5)] for j in range(10)]


def dim10_test_f(x):
    global this_is_the_end
    for x_i in x:
        if abs(x_i) > 10.:
            print(x_i)
    global iterations
    if iterations == 0:
        print("FAIL")
        this_is_the_end = True
    iterations -= 1
    res = min([beta[i] + gamma[i] * sum([(x[j] - alpha_rand[j][i]) ** 2  for j in range(10)]) for i in range(5)])
    if res < 2.01:
        print('Bingo')
        exit(0)
    return res + random() - 0.5

n = int(input())
pop_size, iterations = 100 * n, 10000 * n * n


alpha = 0.5
crossover = 0.8
mutation = 0.1 # y not?


def run(f):

    pop = [[random() * 20. - 10. for i in range(n)] for j in range(pop_size)]
    new_pop = [[0] * n for i in range(pop_size)]
    values = [f(x) for x in pop]
    new_values = [0] * pop_size
    # best = deque([9000.] * (5 * n - 1) + [min(values)])
    # new_best = best[0]
    best = 9000.
    while(True):
        for i in range(pop_size):
            b, c = randint(0, pop_size - 2), randint(0, pop_size - 3)
            if b >= i: b += 1
            if c >= min(i, b): c += 1
            if c >= max(i, b): c += 1
            # gen new candidate
            for j in range(n):
                if random() < crossover:
                    new_pop[i][j] = pop[i][j] + alpha * (pop[b][j] - pop[c][j])
                    if new_pop[i][j] > 10.: new_pop[i][j] = 10.
                    if new_pop[i][j] < -10.: new_pop[i][j] = -10.
                else:
                    new_pop[i][j] = pop[i][j]
            # we've got new candidate
            new_value = f(new_pop[i])
            # if this_is_the_end:
            #     print(best)
            #     exit(0)
            if new_value < values[i]:
                new_values[i] = new_value
                if best > new_value:
                    best = new_value
            else:
                new_values[i] = values[i]
                for j in range(n):
                    new_pop[i][j] = pop[i][j]
        # we dont want to stay at local minimum
        # if best.popleft() - new_best < 0.1:
        #     return new_best # , new_pop[argmin(new_values)]
        # best.append(new_best)
        values, new_values = new_values, values
        pop, new_pop = new_pop, pop
#
# while(True):
#     t = time()
#     res = run(dim10_test_f)
#     alpha += 0.1
#     print("run result:", res, "time:", time() - t, sep='\t')

run(real_f)
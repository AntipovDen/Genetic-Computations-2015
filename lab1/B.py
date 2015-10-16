__author__ = 'Den'

from random import random, randint


def f(x):
    print("".join([str(x_i) + " " for x_i in x]))
    res = input()
    if res == 'Bingo':
        exit(0)
    else:
        return float(res)

n = int(input())
pop_size, iterations = 100 * n

alpha = 0.5
crossover = 0.8

pop = [[random() * 20. - 10. for i in range(n)] for j in range(pop_size)]
new_pop = [[0] * n for i in range(pop_size)]
values = [f(x) for x in pop]
new_values = [0] * pop_size

while (True):
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

        if new_value < values[i]:
            new_values[i] = new_value
        else:
            new_values[i] = values[i]
            for j in range(n):
                new_pop[i][j] = pop[i][j]

    values, new_values = new_values, values
    pop, new_pop = new_pop, pop


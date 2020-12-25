from random import choice
from random import random

LETTERS = "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ" # База возможных генов


# ФОРМИРОВАНИЕ НАЧАЛЬНОЙ ПОПУЛЯЦИИ
def init_population(population_number):
    p = []
    for i in range(population_number):
        gen = choice(LETTERS) + choice(LETTERS) + choice(LETTERS)
        p.append(gen)
    return p


# ОЦЕНИВАНИЕ ПОПУЛЯЦИИ
def fitness(current_population):
    for i, chromosome in enumerate(current_population):
        fit = 1
        if chromosome[0] == "М":
            fit += 1
        if chromosome[1] == "И":
            fit += 1
        if chromosome[2] == "Р":
            fit += 1
        if fit == 4:
            return 1
    return 0


# СКРЕЩИВАНИЕ
def crossover_t(p, pc):
    new_population = []
    for i in range(len(p) - 1):
        parent_1 = choice(p)
        parent_2 = choice(p)
        while parent_1 == parent_2:
            parent_1 = choice(p)  # Формирование первого родителя
            parent_2 = choice(p)  # Формирование второго родителя
        if pc > random():
            child_1 = parent_1[0] + parent_2[1] + parent_1[2]  # Формирование первого потомка
            child_2 = parent_2[0] + parent_1[1] + parent_2[2]  # Формирование второго потомка
            new_population.append(child_1)
            new_population.append(child_2)
        else:
            new_population.append(parent_1)
        i += 2
    return new_population


# МУТАЦИЯ
def mutation(current_population, mutation_chance):
    for i, chromosome in enumerate(current_population):
        for j in range(len(chromosome)):
            if random() < mutation_chance:
                new_gen = choice(LETTERS)
                while current_population[i][j] == new_gen:
                    new_gen = choice(LETTERS)  # Если шанс на мутацию прошел, то меняем ген на любой другой
                current_population[i] = current_population[i].replace(current_population[i][j], new_gen)


# Входная точка программы
if __name__ == '__main__':
    print("Начальная популяция")
    population = init_population(10)  # ФОРМИРОВАНИЕ НАЧАЛЬНОЙ ПОПУЛЯЦИИ
    q = 0
    print(population)
    while q == 0:
        q = fitness(population)  # ОЦЕНИВАНИЕ ПОПУЛЯЦИИ
        population = crossover_t(population, 0.6)  # СКРЕЩИВАНИЕ
        mutation(population, 2)  # МУТАЦИЯ
    print("Слово МИР сгенерировано")
    print("Размер текущей популяции: " + str(len(population)))

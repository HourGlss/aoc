import itertools
from day17_data import data
sizes = []
for line in data.split("\n"):
    sizes.append(int(line))
combos = list(itertools.combinations(sizes, 1))
for i in range(2,len(sizes)-2):
    combos += list(itertools.combinations(sizes, i))
fits = 0
for combo in combos:
    if sum(combo) == 150:
        fits += 1
print(fits)
fits = 0
number_of_containers = 100000
for combo in combos:
    if sum(combo) == 150:
        if len(combo) <number_of_containers:
            number_of_containers = len(combo)
for combo in combos:
    if sum(combo) == 150:
        if len(combo) == number_of_containers:
            fits += 1
print(fits)

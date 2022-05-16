import sys


"""Module for simulating evolution of strings."""
from random import choice, random
from functools import partial

def fitness(trial, target):
    """Compare a string with a target. The more matching characters, the higher the fitness."""
    return sum(t == h for t, h in zip(trial, target))

def mutaterate(parent, target):
    """Calculate a mutation rate that shrinks as the target approaches."""
    perfectfitness = float(len(target))
    return (perfectfitness - fitness(parent, target)) / perfectfitness

def mutate(parent, rate, alphabet):
    """Randomly change characters in parent to random characters from alphabet."""
    return [(ch if random() <= 1 - rate else choice(alphabet)) for ch in parent]

def mate(a, b):
    """
    Split two strings in the center and return 4 combinations of the two:
        1. a
        2. b
        3. beginning of a, then the end of b
        4. beginning of b, then the end of a
    """
    place = int(len(a)/2)
    return a, b, a[:place] + b[place:], b[:place] + a[place:]

def evolve(seed, target_string, alphabet, population_size=100):
    """Randomly mutate populations of seed until it "evolves" into target_string."""

    assert all([l in alphabet for l in target_string]), \
            "Error: Target must only contain characters from alphabet."
    assert len(seed) == len(target_string), \
            "Error: Target and Seed must be the same length."

    # For performance
    target = list(target_string)
    parent = seed
    generations = 0

    while parent != target:
        rate = mutaterate(parent, target)
        mutations = [mutate(parent, rate, alphabet) for _ in range(population_size)] + [parent]

        center = int(population_size/2)
        parent1 = max(mutations[:center], key=partial(fitness, target))
        parent2 = max(mutations[center:], key=partial(fitness, target))
        parent = max(mate(parent1, parent2), key=partial(fitness, target))
        generations += 1
    return generations

seed = sys.argv[1]
target = sys.argv[2]
alphabet = sys.argv[3]

generations = evolve(seed, target, alphabet)
print(f"Success in {generations} generations!")



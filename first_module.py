import math
import random


def get_sum(a, b):
    return a + b


def get_specific_calc(a, b, c):
    return math.pow(get_sum(a, b), c)


def get_random_num():
    return random.choice(range(1, 100))

import math
import random
from routeros import login


def get_sum(a, b):
    return a + b


def get_specific_calc(a, b, c):
    return math.pow(get_sum(a, b), c)


def get_random_num():
    return random.choice(range(1, 100))


def get_info_from_router():
    password = input()
    router_cli = login('admin', password, '192.168.200.1')
    data = router_cli('/ip/pool/print')
    router_cli.close()
    return data


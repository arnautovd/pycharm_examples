import math
import random
from routeros import login
from routeros import utils
import sys


def get_sum(a, b):
    return a + b


def get_specific_calc(a, b, c):
    return math.pow(get_sum(a, b), c)


def get_random_num():
    return random.choice(range(1, 100))


def get_info_from_router():
    password = input('Enter your pass here: ')
    list_of_data = []
    try:
        router_cli = login('admin', password, '192.168.200.1')
        data = router_cli('/ip/arp/print')
        for arp in data:
            list_of_data.append(arp)
        router_cli.close()
        return list_of_data
    except ValueError:
        raise utils.FatalError


def check_the_state():

    states = ['ill', 'healthy']
    state = random.choice(states)
    if state == 'ill':
        print('I want to get a pill')
    print('I am well')


def check_platform():
    assert ('linux' in sys.platform)
    print("Keep going")


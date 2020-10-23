# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from first_module import *


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_hello():
    print('hello again')


def get_info_from(file):
    with open(file, 'r') as f:
        data = f.read()
    return data


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(get_specific_calc(10, 2, 3))
    print(get_info_from('text.txt'))
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

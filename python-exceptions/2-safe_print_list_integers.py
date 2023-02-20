#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    numbers = 0
    for n in range(x):
        try:
            number = my_list[n]
            print("{:d}".format(number), end="")
            numbers = numbers + 1
        except(ValueError, TypeError):
            continue
    print()
    return numbers

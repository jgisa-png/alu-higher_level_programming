#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for index in range(x):
        value = my_list[index]
        try:
            text = "{:d}".format(value)
        except (TypeError, ValueError):
            continue
        print(text, end="")
        count += 1
    print()
    return count

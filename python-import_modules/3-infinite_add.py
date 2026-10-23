#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    total = 0
    for argument in argv[1:]:
        total += int(argument)
    print(total)

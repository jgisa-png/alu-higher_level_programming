#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    results = []
    for index in range(list_length):
        value = 0
        try:
            first = my_list_1[index]
            second = my_list_2[index]
            if not isinstance(first, (int, float)):
                raise TypeError
            if not isinstance(second, (int, float)):
                raise TypeError
            value = first / second
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            results.append(value)
    return results

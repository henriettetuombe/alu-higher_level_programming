#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list_3 = list()
    for k in range(list_length):
        try:
            val = my_list_1[k] / my_list_2[k]
        except ZeroDivisionError:
            val = 0
            print("division by 0")
        except TypeError:
            val = 0
            print("wrong type")
        except IndexError:
            val = 0
            print("out of range")
        finally:
            my_list_3.append(val)
            continue
    return my_list_3

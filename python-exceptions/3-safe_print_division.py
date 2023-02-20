#!/usr/bin/python3
def safe_print_division(a, b):
    div = 1
    try:
        div = a / b

    except:
        div = None
    finally:
        print("Inside result: {}".format(div))
        return div

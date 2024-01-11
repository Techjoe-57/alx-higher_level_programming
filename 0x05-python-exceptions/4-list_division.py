#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    last_list = 0
    for i in range(0, list_length):
        try:
            last_list = my_list_1[i] / my_list_2[i]

        except TypeError:
            last_list = 0
            print("wrong type")

        except ZeroDivisionError:
            last_list = 0
            print("division by 0")
        except IndexError:
            last_list = 0
            print("out of range")
        finally:
            pass
        new_list.append(last_list)
    return new_list

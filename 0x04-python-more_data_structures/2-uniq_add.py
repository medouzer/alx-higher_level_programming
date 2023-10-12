#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_num = set(my_list)
    sum = 0
    for num in uniq_num:
        sum += num
    return sum

#!/usr/bin/python3

somestr = "Eldar Tursunbaev"

def char_frequency(somestr):
    dict = {}
    for n in somestr:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency(somestr))
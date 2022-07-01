#!/usr/bin/python3

somestr = "Eldar Tursunbaev"

def findLen(somestr):
    counter = 0   
    for i in somestr:
        counter += 1
    return counter
 
 
print(findLen(somestr))
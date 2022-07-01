#!/usr/bin/python3
num = int(input("Please enter number"))
list_divisors = []

for i in range(1, num):
    if num % i ==0:
        list_divisors.append(i)
print(list_divisors)
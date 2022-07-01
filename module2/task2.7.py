#!/usr/bin/python3

def tuple_to_int(nums):
    result = int(''.join(map(str,nums)))
    return result

nums = (1,3,2,15)
print("Input:", nums)
print("Output:", tuple_to_int(nums))
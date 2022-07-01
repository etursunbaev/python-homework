#!/usr/bin/python3

some_dict = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print("Input: ",some_dict)
unique_values = set( i for dict in some_dict for i in dict.values())
print("Output: ",sorted(unique_values))
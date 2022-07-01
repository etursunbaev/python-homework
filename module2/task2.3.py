#!/usr/bin/python3
input_items = input("Input comma separated sequence of words")
def sorting(str1):
    words = [word for word in str1.split(",")]
    print(",".join(sorted(list(set(words)))))
sorting(input_items)
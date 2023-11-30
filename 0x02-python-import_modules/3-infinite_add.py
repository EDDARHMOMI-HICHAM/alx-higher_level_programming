#!/usr/bin/python3
from sys import argv

arguments = argv[1:]
result = 0

for arg in arguments:
    result += int(arg)

print(result)

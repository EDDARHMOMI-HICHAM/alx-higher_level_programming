#!/usr/bin/python3
from sys import argv

length = len(argv) - 1
arguments = argv[1:]

if length == 0:
    print("0 arguments.")
elif length == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(length))

for i, arg in enumerate(arguments, start=1):
    print("{}: {}".format(i, arg))

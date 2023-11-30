#!/usr/bin/python3
import dis
import sys

if sys.version_info.major == 3 and sys.version_info.minor == 8:
    with open("hidden_4.pyc", "rb") as f:
        code = compile(f.read(), "hidden_4.pyc", "exec")
        
    for c in code.co_consts:
        if isinstance(c, (str, bytes)) and not c.startswith("__"):
            print(c)
else:
    print("Please run the script in Python 3.8.x.")

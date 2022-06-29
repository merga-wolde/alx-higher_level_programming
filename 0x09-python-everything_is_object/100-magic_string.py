#!/usr/bin/python3
def magic_string():
    return 'BestSchool, ' * (magic_string.calls - 1) + 'BestSchool'
for i in range(10):
    print(magic_string())

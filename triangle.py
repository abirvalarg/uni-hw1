#!/usr/bin/python
height = int(input('N> '))
for y in range(height):
    print(' ' * (height - y - 1) + '*' * (y * 2 + 1))

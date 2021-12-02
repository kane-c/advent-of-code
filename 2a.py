#!/usr/bin/env python3
position = 0
depth = 0

with open('2.txt') as fp:
    for command in fp.readlines():
        word, number = command.split(' ')
        number = int(number)

        if word == 'up':
            depth -= number
        elif word == 'down':
            depth += number
        else:
            position += number

print(depth * position)

#!/usr/bin/env python3
position = 0
depth = 0
aim = 0

with open('2.txt') as fp:
    for command in fp.readlines():
        word, number = command.split(' ')
        number = int(number)

        if word == 'up':
            aim -= number
        elif word == 'down':
            aim += number
        else:
            position += number
            depth += aim * number

print(depth * position)

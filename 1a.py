#!/usr/bin/env python3
previous = 0
increased = 0

with open('1.txt') as fp:
    numbers = tuple(int(line) for line in fp.readlines())

for number in numbers:
    if previous != 0 and number > previous:
        increased += 1

    previous = number

print(increased)

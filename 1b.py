#!/usr/bin/env python3
previous = 0
increased = 0

with open('1.txt') as fp:
    numbers = tuple(int(line) for line in fp.readlines())

for i, number in enumerate(numbers):
    triplet = numbers[i:i + 3]

    if len(triplet) < 3:
        break

    total = sum(triplet)

    if previous != 0 and total > previous:
        increased += 1

    previous = total

print(increased)

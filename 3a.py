#!/usr/bin/env python3
counts = {}

with open('3.txt') as fp:
    for line in fp.readlines():
        for i, bit in enumerate(line):
            if bit == '\n':
                continue
            bit = int(bit)
            counts.setdefault(i, {}).setdefault(bit, 0)
            counts[i][bit] += 1

gamma = []
epsilon = []

for i, bit_counts in counts.items():
    keys = tuple(bit_counts.keys())
    values = tuple(bit_counts.values())
    min_count = min(values)
    max_count = max(values)

    epsilon.append(keys[values.index(min_count)])
    gamma.append(keys[values.index(max_count)])

gamma = int(''.join(str(bit) for bit in gamma), base=2)
epsilon = int(''.join(str(bit) for bit in epsilon), base=2)

print(gamma * epsilon)

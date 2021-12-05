#!/usr/bin/env python3
with open('3.txt') as fp:
    lines = tuple(line.strip() for line in fp.readlines())


def most_least_at_index(lines, i, default):
    counts = {}

    for line in lines:
        bit = int(line[i])
        counts.setdefault(bit, 0)
        counts[bit] += 1

    keys = tuple(counts.keys())
    values = tuple(counts.values())
    co2_count = min(values)
    o2_count = max(values)

    if co2_count == o2_count:
        return default, default

    return keys[values.index(o2_count)], keys[values.index(co2_count)]


filtered_lines_co2 = lines
filtered_lines_o2 = lines

for i in range(len(lines[0])):
    o2_count = len(filtered_lines_o2)
    co2_count = len(filtered_lines_co2)

    if o2_count == 1 and co2_count == 1:
        break

    if o2_count != 1:
        most, _ = most_least_at_index(filtered_lines_o2, i, 1)
        filtered_lines_o2 = [
            line for line in filtered_lines_o2 if int(line[i]) == most
        ]

    if co2_count != 1:
        _, least = most_least_at_index(filtered_lines_co2, i, 0)
        filtered_lines_co2 = [
            line for line in filtered_lines_co2 if int(line[i]) == least
        ]

print(int(filtered_lines_o2[0], base=2) * int(filtered_lines_co2[0], base=2))

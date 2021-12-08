from typing import List, Set

f = open("input8.txt")
all_data = [line for line in f.read().strip().split("\n")]
signal_patterns = list()
output_values = list()
SignalPattern = List[str]
OutputValue = List[str]

for line in all_data:
    sp, ov = line.split(" | ")
    signal_patterns.append(["".join(sorted(x)) for x in sp.split()])
    output_values.append(["".join(sorted(x)) for x in ov.split()])


def part1(output_values: List[OutputValue]) -> int:
    c = 0
    for value in output_values:
        for digit in value:
            if len(digit) in (2, 3, 4, 7):
                c += 1
    return c


def part2(patterns: List[SignalPattern], outputs: List[OutputValue]) -> int:
    total = 0
    for pattern, output in zip(patterns, outputs):
        pattern.sort(key=lambda x: len(x))
        code_to_int = dict()
        for x, y in zip([0, 1, 2, 9], [1, 7, 4, 8]):
            code_to_int.update({pattern[x]: y})
        for x in range(6, 9):
            if not all([(i in pattern[x]) for i in pattern[0]]):
                code_six = pattern[x]
                code_to_int.update({pattern[x]: 6})
            elif all([(i in pattern[x]) for i in pattern[2]]):
                code_to_int.update({pattern[x]: 9})
            else:
                code_to_int.update({pattern[x]: 0})
        for x in range(3, 6):
            if all([(i in pattern[x]) for i in pattern[0]]):
                code_to_int.update({pattern[x]: 3})
            elif all([(i in code_six) for i in pattern[x]]):
                code_to_int.update({pattern[x]: 5})
            else:
                code_to_int.update({pattern[x]: 2})
        assert len(code_to_int) == 10
        for i, x in enumerate(output):
            total += code_to_int[x] * (10 ** (3 - i))
    return total


print(part1(output_values))
print(part2(signal_patterns, output_values))

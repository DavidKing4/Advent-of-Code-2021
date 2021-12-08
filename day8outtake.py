from typing import List, Set

# Your first idea might not always be the best
# our immediate reaction might be to hide our failed attempts
# throughout aoc I have been cleaning up my solutions a little before pushing them.
# I was especially unhappy with this attempt at a solution,
# for transparency this is my first and quite poor attempt of day 8 part 2

f = open("input8.txt")
all_data = [line for line in f.read().strip().split("\n")]
signal_patterns = list()
output_values = list()
SignalPattern = List[Set[chr]]
OutputValue = List[Set[chr]]

for line in all_data:
    sp, ov = line.split(" | ")
    signal_patterns.append([set(x) for x in sp.split()])
    output_values.append([set(x) for x in ov.split()])


def part1(output_values: List[OutputValue]) -> int:
    c = 0
    for value in output_values:
        for digit in value:
            if len(digit) in (2, 3, 4, 7):
                c += 1
    return c


#  0000
# 1    2
# 1    2
#  3333
# 4    5
# 4    5
#  6666
def part2(patterns: List[SignalPattern], outputs: List[OutputValue]) -> int:
    for pattern, value in zip(patterns, outputs):
        decypher = [""] * 7
        int_to_pos = [0] * 10
        code_to_int = dict()
        print(pattern[0])
        code_to_int["".join(list(pattern[0]))] = 1
        code_to_int["".join(list(pattern[1]))] = 7
        code_to_int["".join(list(pattern[2]))] = 4
        code_to_int["".join(list(pattern[9]))] = 8
        print(code_to_int)
        int_to_pos[1] = 0
        int_to_pos[7] = 1
        int_to_pos[4] = 2
        int_to_pos[8] = 10
        pattern.sort(key=lambda x: len(x))
        assert len(pattern[1] - pattern[0]) == 1  # 7 without 1
        decypher[0] = (pattern[1] - pattern[0]).pop()
        for x in range(6, 9):
            # 1 not a subset => 6
            if not all([(i in pattern[x]) for i in pattern[0]]):
                int_to_pos[6] = x
                code_to_int["".join(list(pattern[x]))] = 6
                assert len(pattern[9] - pattern[x]) == 1  # 8 without 6
                decypher[2] = (pattern[9] - pattern[x]).pop()
                decypher[5] = (pattern[1] - set(decypher[0]) - set(decypher[2])).pop()
            # 4 a subset => 9
            elif all([(i in pattern[x]) for i in pattern[2]]):
                code_to_int["".join(list(pattern[x]))] = 9
                int_to_pos[9] = x
                assert len(pattern[9] - pattern[x]) == 1  # 8 without 9
                decypher[4] = (pattern[9] - pattern[x]).pop()
            # if not 6 or 9 must be 0
            else:
                int_to_pos[0] = x
                code_to_int["".join(list(pattern[x]))] = 0
                assert len(pattern[9] - pattern[x]) == 1  # 8 without 0
                decypher[3] = (pattern[9] - pattern[x]).pop()
        for x in range(3, 6):
            # 1 a subset => 3
            if all([(i in pattern[x]) for i in pattern[0]]):
                int_to_pos[3] = x
                code_to_int["".join(list(pattern[x]))] = 3
                fourth_pos = pattern[x]
                fourth_pos -= set(decypher[0])
                fourth_pos -= set(decypher[2])
                fourth_pos -= set(decypher[3])
                fourth_pos -= set(decypher[5])
                assert len(fourth_pos) == 1
                decypher[6] = fourth_pos.pop()
        # 0 take away everything else
        first_pos = pattern[9]
        for l in decypher:
            first_pos -= set(l)
        assert len(first_pos) == 1
        decypher[1] = first_pos.pop()
        print(pattern, decypher, code_to_int)


print(part1(output_values))
part2(signal_patterns, output_values)

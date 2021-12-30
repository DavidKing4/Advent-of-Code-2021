from aoc_timer import aoc_timer


def part1(depths):
    ans1 = sum([1 if depths[i] < depths[i + 1] else 0 for i in range(len(depths) - 1)])
    return ans1


def part2(depths):
    slide = [sum(depths[i : i + 3]) for i in range(len(depths) - 2)]
    ans2 = sum([1 if slide[i] < slide[i + 1] else 0 for i in range(len(slide) - 1)])
    return ans2


def main():
    f = open("input1.txt")
    depths = [int(x) for x in f.read().split("\n")[:-1]]
    print(aoc_timer(part1, [depths], "Part 1: "))
    print(aoc_timer(part2, [depths], "Part 2: "))


if __name__ == "__main__":
    main()

from aoc_timer import aoc_timer


def go(inst, part):
    horiz, depth, aim = 0, 0, 0
    for x, n in inst:
        if part == 1:
            match x:
                case "forward":
                    horiz += int(n)
                case "down":
                    depth += int(n)
                case "up":
                    depth -= int(n)
        if part == 2:
            match x:
                case "forward":
                    horiz += int(n)
                    depth += int(n)*aim
                case "down":
                    aim += int(n)
                case "up":
                    aim -= int(n)
    return(horiz * depth)

def part1(inst):
    return go(inst, part = 1)

def part2(inst):
    return go(inst, part = 2)

def main():
    f = open("input2.txt")
    inst = [x.split() for x in f.read().split("\n")[:-1]]
    print(aoc_timer(part1, [inst], "Part 1: "))
    print(aoc_timer(part2, [inst], "Part 2: "))

if __name__ == "__main__":
    main()
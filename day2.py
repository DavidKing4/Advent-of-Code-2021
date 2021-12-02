from sys import stdin


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


inst = [x.split() for x in stdin]
print(go(inst, part = 1))
print(go(inst, part = 2))
from copy import deepcopy
from datetime import datetime
import time

f = open("input23.txt")
amph = f.read().split("\n")[:-1]

for x in range(len(amph)):
    amph[x] = list(amph[x])


def printable(amph):
    p = ["" for x in range(len(amph))]
    for x in range(len(amph)):
        p[x] = "".join(amph[x])
    return p


def multi_print(s):
    print("  ", end="")
    for i in range(len(s[0])):
        if len(t := str(i)) > 1:
            print(t[0], end="")
        else:
            print(" ", end="")
    print()
    print("  ", end="")
    for i in range(len(s[0])):
        if len(t := str(i)) > 1:
            print(t[1], end="")
        else:
            print(t, end="")
    print()
    for i, l in enumerate(s):
        print(f"{i} {l}")
    print()


def play(amph, log_file):
    log = open(log_file, "w")
    total = 0
    energy = {"A": 1, "B": 10, "C": 100, "D": 1000}
    print("DIY: Nove the amphipods and I'll give you the score!")
    print("Remember to use the least total energy (and don't do anything bold).")
    history = []
    while True:
        print("Score: ", total)
        multi_print(printable(amph))
        print("which amph to move")
        text1 = input("x y: ")
        if text1 == "undo":
            log.write(text1 + "\n")
            total, amph = history.pop()
            continue
        elif text1 == "end":
            log.close()
            return total
        history.append((total, deepcopy(amph)))
        x1, y1 = [int(n) for n in text1.split()]
        t = amph[y1][x1]
        if t not in "ABCD":
            print("I told you not to be bold...")
            time.sleep(0.5)
            continue
        print("move to where?")
        text2 = input("x y: ")
        x2, y2 = [int(n) for n in text2.split()]
        if amph[y2][x2] != ".":
            print("cop on")
            time.sleep(0.5)
            continue
        log.write(text1 + "\n")
        log.write(text2 + "\n")
        d = abs(y1 - 1) + abs(y2 - 1) + abs(x1 - x2)
        total += energy[t] * d
        amph[y1][x1] = "."
        amph[y2][x2] = t
        print()


print(play(amph, str(datetime.today()).replace(":", "")[:17] + "day23p1.sol"))
amph = amph[:3] + [list("  #D#C#B#A#")] + [list("  #D#B#A#C#")] + amph[3:]
print(play(amph, str(datetime.today()).replace(":", "")[:17] + "day23p2.sol"))

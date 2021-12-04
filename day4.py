from copy import deepcopy
from typing import List, Union


f = open("input4e.txt")
all_data = [x for x in f.read().split("\n\n")]
balls = [int(x) for x in all_data[0].split(",")]
all_boards = [[[0] * 5 for _ in range(5)] for _ in range(len(all_data) - 1)]
for b, board in enumerate(all_data[1:]):
    for x, line in enumerate(board.split("\n")):
        for y, num in enumerate(line.split()):
            all_boards[b][x][y] = int(num)


def calc_score(board: List[List[List[int]]], called: int) -> int:
    score = sum([x if x != -1 else 0 for y in board for x in y])
    score *= called
    return score


def check_bingo(board: List[List[List[int]]]) -> bool:
    if -5 in [sum(x) for x in board]:
        return True
    elif -5 in [sum([board[x][y] for x in range(5)]) for y in range(5)]:
        return True
    return False


def check_num(
    boards: List[List[List[int]]], called: int
) -> Union[List[List[List[int]]], int]:
    for b in range(len(boards)):
        for x in range(5):
            for y in range(5):
                if boards[b][x][y] == called:
                    boards[b][x][y] = -1
                    if check_bingo(boards[b]):
                        return b
    return boards


def part1(balls: List[int], boards: List[List[List[int]]]) -> int:
    for num in balls:
        b = check_num(boards, num)
        if isinstance(b, int):
            return calc_score(boards[b], num)
        else:
            boards = b


def part2(balls: List[int], boards: List[List[List[int]]]) -> int:
    for num in balls:
        b = check_num(boards, num)
        while isinstance(b, int):
            if len(boards) == 1:
                return calc_score(boards[0], num)
            del boards[b]
            b = check_num(boards, num)
        boards = b
    print(len(boards))


print(part1(balls, deepcopy(all_boards)))
print(part2(balls, deepcopy(all_boards)))

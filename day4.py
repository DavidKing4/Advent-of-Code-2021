from aoc_timer import aoc_timer
from copy import deepcopy
from typing import List, Union
from timeit import timeit

Board = List[List[int]]


def calc_score(board: List[Board], called: int) -> int:
    score = sum([x if x != -1 else 0 for y in board for x in y])
    score *= called
    return score


def check_bingo(board: List[Board]) -> bool:
    if -5 in [sum(x) for x in board]:
        return True
    elif -5 in [sum([board[x][y] for x in range(5)]) for y in range(5)]:
        return True
    return False


def check_num(boards: List[Board], called: int) -> Union[List[Board], int]:
    for b in range(len(boards)):
        for x in range(5):
            for y in range(5):
                if boards[b][x][y] == called:
                    boards[b][x][y] = -1
                    if check_bingo(boards[b]):
                        return b
    return boards


def part1(balls: List[int], boards: List[Board]) -> int:
    for num in balls:
        b = check_num(boards, num)
        if isinstance(b, int):
            return calc_score(boards[b], num)
        else:
            boards = b


def part2(balls: List[int], boards: List[Board]) -> int:
    for num in balls:
        b = check_num(boards, num)
        while isinstance(b, int):
            if len(boards) == 1:
                return calc_score(boards[0], num)
            del boards[b]
            b = check_num(boards, num)
        boards = b
    print(len(boards))


def main():
    f = open("input4.txt")
    all_data = [x for x in f.read().split("\n\n")]
    balls = [int(x) for x in all_data[0].split(",")]
    all_boards = [[[0] * 5 for _ in range(5)] for _ in range(len(all_data) - 1)]
    for b, board in enumerate(all_data[1:]):
        for x, line in enumerate(board.split("\n")):
            for y, num in enumerate(line.split()):
                all_boards[b][x][y] = int(num)
    name = __name__
    boards = deepcopy(all_boards)
    print(aoc_timer(part1, (balls, boards), "Part1: "))
    boards = deepcopy(all_boards)
    print(aoc_timer(part2, (balls, boards), "Part2: "))


if __name__ == "__main__":
    main()

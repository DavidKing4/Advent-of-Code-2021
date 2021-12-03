from sys import stdin
import numpy as np

dio = np.array([[int(x) for x in line.strip()] for line in stdin])
truthy = np.sum(dio, 0) > dio.shape[0] / 2
falsey = np.logical_not(truthy)
gamma = int("".join([str(int(x)) for x in truthy]), 2)
epsilon = int("".join([str(int(x)) for x in falsey]), 2)
print("Part 1:", gamma * epsilon)


def array_filter(dio, column, mode):  # mode 0 = keep 0, mode 1 = keep 1
    return dio[dio[:, column] == mode]


def find_common_filter(dio, column, oxorco):  # 0 = ox, 1 = co2
    c = np.sum(dio, 0)[column]
    l = dio.shape[0] / 2
    if c == l:
        return array_filter(dio, column, 1 - oxorco)
    if c < l:
        return array_filter(dio, column, 0 + oxorco)
    if c > l:
        return array_filter(dio, column, 1 - oxorco)


def get_rating(dio, ox_or_co):
    for x in range(dio.shape[1]):
        dio = find_common_filter(dio, x, ox_or_co)
        if dio.shape[0] == 1:
            return int("".join([str(x) for x in dio[0]]), 2)


ox = get_rating(dio.copy(), 0)
co = get_rating(dio.copy(), 1)
print("Part 2:", ox * co)

from math import ceil
from typing import Generic, Tuple, TypeVar, Union, Optional

f = open("input18.txt")
raw_data = f.read()[:-1].split("\n")

SFNum = TypeVar("SFNum")


class SFN(Generic[SFNum]):
    depth: int
    left_child: Union[int, SFNum]
    right_child: Union[int, SFNum]
    parent: SFNum

    def __init__(self, depth: int, num: str, parent: Optional[SFNum] = None) -> None:
        self.depth = depth
        assert isinstance(num, str), "you're doing it wrong dumbo"
        self.left_child, self.right_child = self.str_to_sfnum(num)
        self.parent = parent

    def str_to_sfnum(self, num: str) -> Tuple[SFNum]:
        ob_counter = 0
        middle = -1
        for i, x in enumerate(num):
            if x == "[":
                ob_counter += 1
            elif x == "]":
                ob_counter -= 1
            elif x == "," and ob_counter == 1:
                middle = i
                break
        assert middle != -1
        left = num[1:i]
        right = num[i + 1 : -1]
        left_child = None
        right_child = None

        if left.isnumeric():
            left_child = int(left)
        else:
            left_child = SFN(self.depth + 1, left, self)

        if right.isnumeric():
            right_child = int(right)
        else:
            right_child = SFN(self.depth + 1, right, self)

        return (left_child, right_child)

    def printable(self) -> str:
        if isinstance(self.left_child, int):
            left = str(self.left_child)
        else:
            left = self.left_child.printable()
        if isinstance(self.right_child, int):
            right = str(self.right_child)
        else:
            right = self.right_child.printable()
        return f"[({self.depth}){left},{right}]"

    def increase_depth(self) -> None:
        self.depth += 1
        if not isinstance(self.left_child, int):
            self.left_child.increase_depth()
        if not isinstance(self.right_child, int):
            self.right_child.increase_depth()

    def add(self, num) -> SFNum:
        result = SFN(self.depth, "[0,0]")
        result.left_child = self
        result.left_child.parent = result
        result.right_child = num
        result.right_child.parent = result
        result.left_child.increase_depth()
        result.right_child.increase_depth()
        while result.reduce():
            pass
        return result

    def explode_left(self) -> None:
        cur = self
        nxt = self.parent
        while nxt.left_child == cur:
            if nxt.parent is None:
                return
            cur = nxt
            nxt = nxt.parent
        if isinstance(nxt.left_child, int):
            nxt.left_child += self.left_child
            return
        cur = nxt.left_child
        while not isinstance(cur.right_child, int):
            cur = cur.right_child
        cur.right_child += self.left_child

    def explode_right(self) -> None:
        cur = self
        nxt = self.parent
        while nxt.right_child == cur:
            if nxt.parent is None:
                return
            cur = nxt
            nxt = nxt.parent
        if isinstance(nxt.right_child, int):
            nxt.right_child += self.right_child
            return
        cur = nxt.right_child
        while not isinstance(cur.left_child, int):
            cur = cur.left_child
        cur.left_child += self.right_child

    def explode(self) -> None:
        self.explode_left()
        self.explode_right()
        if self.parent.left_child == self:
            self.parent.left_child = 0
        if self.parent.right_child == self:
            self.parent.right_child = 0

    def split(self) -> None:
        if isinstance(self.left_child, int) and self.left_child > 9:
            self.left_child = SFN(
                self.depth + 1,
                f"[{self.left_child//2},{ceil(self.left_child/2)}]",
                self,
            )
        elif isinstance(self.right_child, int) and self.right_child > 9:
            self.right_child = SFN(
                self.depth + 1,
                f"[{self.right_child//2},{ceil(self.right_child/2)}]",
                self,
            )

    def reduce(self) -> bool:
        if self.reduce_explode():
            return True
        if self.reduce_split():
            return True

    def reduce_explode(self) -> bool:
        if self.depth >= 4:
            self.explode()
            return True
        if isinstance(self.left_child, SFN):
            if self.left_child.reduce_explode():
                return True
        if isinstance(self.right_child, SFN):
            if self.right_child.reduce_explode():
                return True

    def reduce_split(self) -> bool:
        if isinstance(self.left_child, int):
            if self.left_child > 9:
                self.split()
                return True
        else:
            if self.left_child.reduce_split():
                return True
        if isinstance(self.right_child, int):
            if self.right_child > 9:
                self.split()
                return True
        else:
            if self.right_child.reduce_split():
                return True

    def magnitude(self) -> int:
        mag = 0
        if isinstance(self.left_child, int):
            mag += 3 * self.left_child
        else:
            mag += 3 * self.left_child.magnitude()
        if isinstance(self.right_child, int):
            mag += 2 * self.right_child
        else:
            mag += 2 * self.right_child.magnitude()
        return mag


def part1(data) -> int:
    num = SFN(0, data[0])
    for x in data[1:]:
        num = num.add(SFN(0, x))
    return num.magnitude()


def part2(data) -> int:
    biggest = 0
    for x in data:
        for y in data:
            if x != y:
                t = SFN(0, x)
                t = t.add(SFN(0, y))
                if (b := t.magnitude()) > biggest:
                    biggest = b
    return biggest


print(part1(raw_data))
print(part2(raw_data))

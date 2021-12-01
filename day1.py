f = open("input1.txt")
depths = [int(x) for x in f.read().split("\n")[:-1]]
ans1 = sum([1 if depths[i] < depths[i + 1] else 0 for i in range(len(depths) - 1)])
print(ans1)

slide = [sum(depths[i : i + 3]) for i in range(len(depths) - 2)]
ans2 = sum([1 if slide[i] < slide[i + 1] else 0 for i in range(len(slide) - 1)])
print(ans2)

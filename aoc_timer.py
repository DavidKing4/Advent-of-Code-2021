from time import perf_counter


def aoc_timer(func, args=[], text=""):
    start = perf_counter()
    ans = func(*args)
    end = perf_counter()
    timer = end - start
    with_unit = ""
    if timer > 1:
        with_unit = f"\t{timer:.02f}s"
    if timer > 10 ** -3:
        with_unit = f"\t{(timer * 10**3):.02f}ms"
    else:
        with_unit = f"\t{(timer * 10**6):.02f}µs"
    return text + str(ans) + with_unit

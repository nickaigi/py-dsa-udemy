def sum_slow(n: int) -> int:
    total = 0
    for i in range(n):
        total += i
    return total


def sum_fast(n: int) -> int:
    return int((n * (n + 1)) / 2)


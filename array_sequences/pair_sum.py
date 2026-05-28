def pair_sum(arr: list[int], k: int):
    if len(arr) < 2:
        return

    seen = set()
    output = set()
    for num in arr:
        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))
    return len(output)


if __name__ == "__main__":
    assert pair_sum([1, 3, 2, 2], 4) == 2

"""
Given a string in the form "AAAABBBBCCCCCDDEEEE" compress it to become "A4B4C5D2E4".
For this problem, you can falsely "compress" strings of single or double letters.
For instance, it is okay for "AAB" to return "A2B1" even though this technically takes more space.

The function should be case sensitive, so that a string "AAAaaa" returns "A3a3"
"""

from collections import defaultdict


def str_compress(s: str) -> str:
    d = defaultdict(int)
    for char in s:
        d[char] += 1
    return "".join([f"{k}{v}" for k, v in d.items()])


if __name__ == "__main__":
    s = "AAAABBBBCCCCCDDEEEE"
    assert str_compress(s) == "A4B4C5D2E4"
    s = "AAB"
    assert str_compress(s) == "A2B1"
    s = "AAAaaa"
    assert str_compress(s) == "A3a3"
    print("All Tests Passed")

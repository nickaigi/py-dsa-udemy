"""
Given a string, determine if it comprises of all unique characters.
E.g.
    "abcde" has all unique characters and should return True.
    "aabcde" contains duplicate characters and should return False.
"""


def uni_char(s: str) -> bool:
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True


def uni_chars(s: str) -> bool:
    return len(set(s)) == len(s)


if __name__ == "__main__":
    assert uni_char("abcde")
    assert not uni_char("aabcde")
    print("All Tests Passed")

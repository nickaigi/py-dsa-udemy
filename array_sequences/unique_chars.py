"""
Given a string, determine if it comprises of all unique characters.
E.g.
    "abcde" has all unique characters and should return True.
    "aabcde" contains duplicate characters and should return False.
"""


def uni_char(s: str) -> bool:
    seen: list[str] = []
    for char in s:
        if char in seen:
            return False
        seen.append(char)
    return True


if __name__ == "__main__":
    assert uni_char("abcde")
    assert not uni_char("aabcde")
    print("All Tests Passed")

"""
Given a string in the form "AAAABBBBCCCCCDDEEEE" compress it to become "A4B4C5D2E4".
For this problem, you can falsely "compress" strings of single or double letters.
For instance, it is okay for "AAB" to return "A2B1" even though this technically takes more space.

The function should be case sensitive, so that a string "AAAaaa" returns "A3a3"
"""


def compress(s: str) -> str:
    """
    Run length Algorithm
    """
    r = ""
    n = len(s)

    if n == 0:  # edge case where string is empty
        return ""
    if n == 1:  # edge case where string has 1 letter
        return s + "1"

    count = 1
    i = 1

    while i < n:
        if s[i] == s[i - 1]:
            count += 1
        else:
            r = r + s[i - 1] + str(count)
            count = 1
        i += 1

    r = r + s[i - 1] + str(count)
    return r


if __name__ == "__main__":
    s = "AAAABBBBCCCCCDDEEEE"
    assert compress(s) == "A4B4C5D2E4"
    s = "AAB"
    assert compress(s) == "A2B1"
    s = "AAAaaa"
    assert compress(s) == "A3a3"
    print("All Tests Passed")

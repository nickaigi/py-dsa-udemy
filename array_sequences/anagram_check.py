def anagram(s1: str, s2: str) -> bool:
    s1 = "".join([c.lower() for c in s1 if c != " "])
    s2 = "".join([c.lower() for c in s2 if c != " "])

    if len(s1) != len(s2):
        return False

    data = {}
    for char in s1:
        data[char] = data.get("char", 0) + 1
    for char in s2:
        if char not in data:
            return False
        data[char] -= 1
    return True


if __name__ == "__main__":
    assert anagram("dog", "god")
    assert anagram("go go go", "gggooo")
    assert anagram("abc", "cba")
    assert anagram("hi man", "hi      man")
    assert not anagram("aabbcc", "aabbc")
    assert not anagram("123", "1 2")
    assert anagram("", "")
    print("ALL TEST CASES PASSED")

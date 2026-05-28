def anagram(s1: str, s2: str) -> bool:
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False
    counter = {}

    for char in s1:
        counter[char] = counter.get(char, 0) + 1
    for char in s2:
        if char not in counter or counter[char] == 0:
            return False
        counter[char] -= 1
    return True


if __name__ == "__main__":
    assert anagram("dog", "god")
    assert anagram("go go go", "gggooo")
    assert anagram("abc", "cba")
    assert anagram("hi man", "hi      man")
    assert not anagram("aabbcc", "aabbc")
    assert not anagram("123", "1 2")
    assert anagram("", "")
    assert anagram("clint eastwood", "old west action")
    print("ALL TEST CASES PASSED")

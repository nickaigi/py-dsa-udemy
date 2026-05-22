def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    counter = {}
    for char in s:
        counter[char] = counter.get(char, 0) + 1
    for char in t:
        if char not in counter or counter[char] == 0:
            return False
        counter[char] -= 1
    return True


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"

    assert is_anagram(s, t)

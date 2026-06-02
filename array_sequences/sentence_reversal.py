def rev_word1(s: str) -> str:
    return " ".join(reversed(s.split()))


def rev_word2(s: str) -> str:
    return " ".join(s.split()[::-1])


def rev_word3(s: str) -> str:
    """split on the spaces"""
    words = []
    str_len = len(s)
    i = 0

    while i < str_len:
        if s[i] != " ":
            word_start = i
            while i < str_len and s[i] != " ":
                i += 1

            words.append(s[word_start:i])
        i += 1
    return " ".join(reversed(words))


if __name__ == "__main__":
    s: str = "    Hello John    how are you     "
    assert rev_word1(s) == "you are how John Hello"
    assert rev_word2(s) == "you are how John Hello"
    assert rev_word3(s) == "you are how John Hello"
    print("All Tests Passed")

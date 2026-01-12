def word_break(s: str, words: list[str]) -> bool:
    if len(s) == 0:
        return True

    for word in words:
        if len(word) > len(s):
            continue

        prefix = s[:len(word)]
        if prefix == word:
            return word_break(s[len(word):], words)

    return False

if __name__ == "__main__":
    s = input()
    words = input().split()
    res = word_break(s, words)
    print("true" if res else "false")

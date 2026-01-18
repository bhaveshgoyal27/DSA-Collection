from collections import deque

def word_ladder(begin: str, end: str, word_list: list[str]) -> int:
    word_set = set(word_list)
    if end not in word_set:
        return -1

    begin_set = {begin}
    end_set = {end}
    visited = set()
    level = 1
    L = len(begin)

    while begin_set and end_set:
        # Always expand the smaller frontier
        if len(begin_set) > len(end_set):
            begin_set, end_set = end_set, begin_set

        next_set = set()

        for word in begin_set:
            for i in range(L):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + c + word[i+1:]

                    if new_word in end_set:
                        return level

                    if new_word in word_set and new_word not in visited:
                        visited.add(new_word)
                        next_set.add(new_word)

        begin_set = next_set
        level += 1

    return -1


if __name__ == "__main__":
    begin = input()
    end = input()
    word_list = input().split()
    res = word_ladder(begin, end, word_list)
    print(res)

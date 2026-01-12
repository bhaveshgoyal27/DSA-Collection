def letter_combination(n: int) -> list[str]:
    path =[""]
    for _ in range(n):
        t = []
        for i in path:
            t.append(i+"a")
            t.append(i+"b")
        path = t
    return path

if __name__ == "__main__":
    n = int(input())
    res = letter_combination(n)
    for line in sorted(res):
        print(line)



####### Try doing dfs approach


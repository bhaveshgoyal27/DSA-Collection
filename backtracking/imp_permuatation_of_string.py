def permutations(letters: str) -> list[str]:
    answers = []
    n = len(letters)
    used = [0]*n
    def dfs(path):
        if len(path) == n:
            answers.append(path)
            return
        for i in range(n):
            if used[i]==0:
                used[i]+=1
                path += letters[i]
                dfs(path)
                path = path[:-1]
                used[i]-=1
    dfs("")
    return answers

if __name__ == "__main__":
    letters = input()
    res = permutations(letters)
    for line in sorted(res):
        print(line)

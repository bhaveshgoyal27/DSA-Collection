def partition(s: str) -> list[list[str]]:
    n = len(s)
    res = []
    def check_palindrome(s1):
        if not s1:
            return True
        i, j = 0, len(s1)-1
        while i<j:
            if s1[i]!=s1[j]:
                return False
            i+=1
            j-=1
        return True
    def dfs(start, cur_path):
        if start == n:
            res.append(cur_path[:])
            return

        for end in range(start + 1, n + 1):
            prefix = s[start:end]
            if check_palindrome(prefix):
                dfs(end, cur_path + [prefix])

    dfs(0, [])
    return res
    # WRITE YOUR BRILLIANT CODE HERE
    return []

partition("aab")
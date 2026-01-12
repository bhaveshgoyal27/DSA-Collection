def subsets(nums: list[int]) -> list[list[int]]:
    ans = []
    def dfs(i=0, curr=[]):
        if i == len(nums):
            ans.append(curr)
            return

        dfs(i + 1, curr)
        dfs(i + 1, curr + [nums[i]])

    dfs()
    return ans
from collections import Counter
def find_all_anagrams(original: str, check: str) -> list[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    ans = []
    l1 = len(original)
    l2 = len(check)
    check_dict = Counter(check)
    window = Counter()

    i = 0
    for j in range(l1):
        window[original[j]]+=1
        if j-i == l2:
            window[original[i]]-=1
            i+=1
        if j-i+1 == l2:
            if window == check_dict:
                ans.append(i)
    return ans


ori = "cbaebabacd"
ch = "abc"

# ori = "abab"
# ch = "ab"
print(find_all_anagrams(ori, ch))
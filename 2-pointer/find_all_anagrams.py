def find_all_anagrams(original: str, check: str) -> list[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    i=j=0
    ans = []
    l1 = len(original)
    l2 = len(check)
    check_dict = {}
    for k in check:
        if k in check_dict:
            check_dict[k]+=1
        else:
            check_dict[k] = 1
    while(i<l1-l2):
        new_check = check_dict.copy()
        c1 = True
        for j in range(i, i+l2):
            if new_check.get(original[j]):
                new_check[original[j]]-=1
            else:
                i=j
                c1 = False
                break
        if c1:
            ans.append(i)
            i+=1


    return ans

ori = "cbaebabacd"
ch = "abc"

ori = "abab"
ch = "ab"
print(find_all_anagrams(ori, ch))
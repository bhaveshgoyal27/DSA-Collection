from collections import Counter

def verify_count(window, check_counter):
    for i in check_counter:
        if check_counter[i]>window.get(i, 0):
            return False
    return True

def get_min(str1, str2):
    if len(str1)>len(str2):
        return str2
    elif len(str2)>len(str1):
        return str1
    else:
        return min(str1, str2)


def get_minimum_window(original: str, check: str) -> str:
    check_counter = Counter(check)
    window = Counter()
    i = 0
    ans = original
    flag = False
    for j in range(len(original)):
        if check_counter.get(original[j]):
            window[original[j]] +=1
        while verify_count(window, check_counter):
            flag = True
            ans = get_min(ans, original[i:j+1])
            if check_counter.get(original[i]):
                window[original[i]]-=1
            i+=1
    if not flag:
        return ""
    return ans


##### TO BE OPTIMIZED



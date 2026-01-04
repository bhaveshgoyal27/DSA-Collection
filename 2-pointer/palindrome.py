def is_palindrome(s: str) -> bool:
    l, r = 0, len(s)-1
    while l < r:
        if s[l].isalnum() and s[r].isalnum() and s[l].lower() != s[r].lower(): return False
        elif s[l].isalnum() and not s[r].isalnum(): r -= 1
        elif not s[l].isalnum() and s[r].isalnum(): l += 1
        else:
            l += 1
            r -= 1
    return True
def longest_substring_without_repeating_characters(s: str) -> int:
    length = 0
    left = 0
    window = set()
    for right in range(len(s)):
        while s[right] in window:
            window.remove(s[left])
            left += 1
        window.add(s[right])
        length = max(length, right - left + 1)
    return length
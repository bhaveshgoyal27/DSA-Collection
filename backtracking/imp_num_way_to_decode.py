def decode_ways(digits: str) -> int:
    if len(digits)<=1:
        return 1

    if digits[0] =="0":
        return 0

    a = int( digits[0:2])
    ans = 0
    if 10<=a<=26:
        ans += decode_ways(digits[2:])
    ans += decode_ways(digits[1:])

    return ans


print(decode_ways("12"))
print(decode_ways("123"))
print(decode_ways("11223"))
print(decode_ways("313"))
print(decode_ways("02"))


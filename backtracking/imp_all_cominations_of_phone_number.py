def letter_combinations_of_phone_number(digits: str) -> list[str]:
    if not digits:
        return []
    data = dict()
    data["2"] = ["a", "b", "c"]
    data["3"] = ["d", "e", "f"]
    data["4"] = ["g", "h", "i"]
    data["5"] = ["j", "k", "l"]
    data["6"] = ["m", "n", "o"]
    data["7"] = ["p", "q", "r", "s"]
    data["8"] = ["t", "u", "v"]
    data["9"] = ["w", "x", "y", "z"]
    res = []
    path = ""
    def get_digits(digits, path):
        if digits == "":
            res.append(path)
            return 
        for i in data[str(digits[0])]:
            path += i
            get_digits(digits[1:], path)
            path = path[:-1]

    get_digits(digits, path)
    # WRITE YOUR BRILLIANT CODE HERE
    return res

letter_combinations_of_phone_number("56")
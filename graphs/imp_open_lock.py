from collections import deque

def num_steps(target_combo: str, trapped_combos: list[str]) -> int:
    if target_combo == "0000":
        return 0

    trapped = set(trapped_combos)
    if "0000" in trapped:
        return -1

    visited = {"0000"}
    queue = deque([("0000", 0)])

    while queue:
        combo, dist = queue.popleft()

        for i in range(4):
            digit = int(combo[i])

            for new_digit in ((digit + 1) % 10, (digit - 1) % 10):
                new_combo = (
                        combo[:i] + str(new_digit) + combo[i + 1 :]
                )

                if new_combo == target_combo:
                    return dist + 1

                if new_combo not in trapped and new_combo not in visited:
                    visited.add(new_combo)
                    queue.append((new_combo, dist + 1))

    return -1

if __name__ == "__main__":
    target_combo = input()
    trapped_combos = input().split()
    res = num_steps(target_combo, trapped_combos)
    print(res)

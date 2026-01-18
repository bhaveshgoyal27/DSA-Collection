from collections import deque
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

INF = 2147483647

def map_gate_distances(dungeon_map: list[list[int]]) -> list[list[int]]:
    queue: deque[tuple[int, int]] = deque()
    n = len(dungeon_map)
    m = len(dungeon_map[0])
    for i, map_row in enumerate(dungeon_map):
        for j, entry in enumerate(map_row):
            if entry == 0:
                queue.append((i, j))
    while queue:
        row, col = queue.popleft()
        for delta_row, delta_col in directions:
            total_row, total_col = row + delta_row, col + delta_col
            if total_row >= 0 and total_row < n and total_col >= 0 and total_col < m:
                if dungeon_map[total_row][total_col] == INF:
                    dungeon_map[total_row][total_col] = dungeon_map[row][col] + 1
                    queue.append((total_row, total_col))
    return dungeon_map

if __name__ == "__main__":
    dungeon_map = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = map_gate_distances(dungeon_map)
    for row in res:
        print(" ".join(map(str, row)))

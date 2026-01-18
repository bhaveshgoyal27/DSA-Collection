from collections import deque
def count_number_of_islands(grid: list[list[int]]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    no_islands = 0
    m, n = len(grid), len(grid[0])
    visited = [[0] * n for _ in range(m)]
    total_visted = 0
    total_sum = 0
    for i in range(m):
        total_sum += sum(grid[i])
    que = deque()
    def get_start():
        for i in range(m):
            for j in range(n):
                if grid[i][j] and not visited[i][j]:
                    return True, i,j
        return False, None, None
    def bfs(total_visted):
        while que:
            a,b = que.popleft()
            movements = [(-1,0), (0,1), (1,0), (0,-1)]
            for move in movements:
                dx, dy = a+move[0], b+move[1]
                if 0<=dx<m and 0<=dy<n and grid[dx][dy]==1 and visited[dx][dy]==0:
                    visited[dx][dy]=1
                    total_visted +=1
                    que.append((dx,dy))
        return total_visted
    while total_visted!= total_sum:
        status, start_x, start_y = get_start()
        if not status:
            return no_islands
        visited[start_x][start_y]=1
        total_visted +=1
        que.append((start_x, start_y))
        total_visted = bfs(total_visted)
        no_islands +=1
    return no_islands

if __name__ == "__main__":
    grid = [[1,1, 1, 0, 0, 0],[1,1, 1, 1, 0, 0],[1,1, 1, 0, 0, 0],[0,1, 0, 0, 0, 0],[0,0, 0, 0, 1, 0],[0,0, 0, 0, 0, 0]]
    res = count_number_of_islands(grid)
    print(res)



from collections import deque
def get_knight_shortest_path(x: int, y: int) -> int:
    moves = [(-1,-2), (-2,-1), (-1,2), (-2,1), (1,2), (2,1), (1,-2), (2,-1)]
    que = deque()
    que.append((0,0))
    lvl = 0
    visited = set()
    while que:
        n = len(que)
        for _ in range(n):
            curr_x, curr_y = que.popleft()
            if curr_x == x and curr_y == y:
                return lvl
            else:
                for move in moves:
                    dx = curr_x+move[0]
                    dy = curr_y+move[1]
                    if (dx,dy) not in visited:
                        visited.add((dx, dy))
                        que.append((dx,dy))
        lvl+=1


    # WRITE YOUR BRILLIANT CODE HERE
    return lvl

if __name__ == "__main__":
    x = int(input())
    y = int(input())
    res = get_knight_shortest_path(x, y)
    print(res)

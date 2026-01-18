from collections import deque
def flood_fill(r: int, c: int, replacement: int, image: list[list[int]]) -> list[list[int]]:
    # WRITE YOUR BRILLIANT CODE HERE
    m, n = len(image), len(image[0])
    original = image[r][c]
    if original == replacement:
        return image
    image[r][c] = replacement
    queue = deque([(r,c)])
    while queue:
        x,y = queue.popleft()
        movements = [(-1,0), (0,1), (1,0), (0,-1)]
        for move in movements:
            dx = x+move[0]
            dy = y+move[1]
            if 0<=dx<m and 0<=dy<n and image[dx][dy]==original:
                image[dx][dy] = replacement
                queue.append((dx,dy))

    return image

if __name__ == "__main__":
    r = int(input())
    c = int(input())
    replacement = int(input())
    image = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = flood_fill(r, c, replacement, image)
    for row in res:
        print(" ".join(map(str, row)))

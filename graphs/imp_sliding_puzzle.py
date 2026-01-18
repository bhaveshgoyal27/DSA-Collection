from collections import deque
def num_steps(init_pos: list[list[int]]) -> int:
    def check():
        valid = [[1,2,3], [4,5,0]]
        return init_pos == valid
    m, n = 2,3
    posx = posy = 0
    moves = 0
    moved = False
    for i in range(m):
        for j in range(n):
            if init_pos[i][j] ==0:
                posx, posy = i, j
                break
    while not check():
        pass

    # WRITE YOUR BRILLIANT CODE HERE
    return 0

if __name__ == "__main__":
    init_pos = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = num_steps(init_pos)
    print(res)

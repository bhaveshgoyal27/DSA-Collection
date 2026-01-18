from collections import deque

def shortest_path(graph: list[list[int]], a: int, b: int) -> int:
    if a==b or a>len(graph) or b>len(graph) or a<0 or b<0:
        return 0
    visited = set()
    queue = deque()
    def bfs():
        lvl = 0
        while len(queue):
            n = len(queue)
            for _ in range(n):
                curr_node = queue.popleft()
                if curr_node == b:
                    return lvl
                for neighbor in graph[curr_node]:
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
            lvl+=1
        return 0
    queue.append(a)
    visited.add(a)
    level = bfs()
    # WRITE YOUR BRILLIANT CODE HERE

    return level

if __name__ == "__main__":
    graph = [[int(x) for x in input().split()] for _ in range(int(input()))]
    a = int(input())
    b = int(input())
    res = shortest_path(graph, a, b)
    print(res)

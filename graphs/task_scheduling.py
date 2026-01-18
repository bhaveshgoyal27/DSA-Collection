import sys
from collections import deque

def task_scheduling(tasks: list[str], requirements: list[list[str]]) -> list[str]:
    # WRITE YOUR BRILLIANT CODE HERE
    inmatrix_dict = {x:0 for x in tasks}
    graph = dict()
    for req, task in requirements:
        inmatrix_dict[task]+=1
        if req in graph:
            graph[req].append(task)
        else:
            graph[req] = [task]
    que = deque()
    res = []
    for node in inmatrix_dict:
        if inmatrix_dict[node]==0:
            que.append(node)
    while que:
        node = que.popleft()
        res.append(node)
        for task in graph.get(node, []):
            inmatrix_dict[task]-=1
            if inmatrix_dict[task]==0:
                que.append(task)


    return res

if __name__ == "__main__":
    tasks = input().split()
    requirements = [input().split() for _ in range(int(input()))]
    res = task_scheduling(tasks, requirements)
    if len(res) != len(tasks):
        print(f"output size {len(res)} does not match input size {len(tasks)}")
        sys.exit()
    indices = {task: i for i, task in enumerate(res)}
    for req in requirements:
        for task in req:
            if task not in indices:
                print(f"'{task}' is not in output")
                sys.exit()
        a, b = req
        if indices[a] >= indices[b]:
            print(f"'{a}' is not before '{b}'")
            sys.exit()
    print("ok")

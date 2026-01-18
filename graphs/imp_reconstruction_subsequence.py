from collections import deque
def sequence_reconstruction(original: list[int], seqs: list[list[int]]) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    def inmat(graph):
        matrix = {node: 0 for node in graph}
        for node in graph:
            for dest in graph[node]:
                matrix[dest]+=1
        return matrix

    def topological(graph):
        inmatrix = inmat(graph)
        que = deque()
        for i in inmatrix:
            if inmatrix[i] == 0:
                que.append(i)
        while que:
            if len(que)>1:
                return False
            node = que.popleft()
            for targt in graph[node]:
                inmatrix[targt]  -=1
                if inmatrix[targt] == 0:
                    que.append(targt)
        return True

    graph = {node: set() for node in original}
    for seq in seqs:
        for i in range(len(seq)-1):
            graph[seq[i]].add(seq[i+1])
    return topological(graph)

if __name__ == "__main__":
    original = [int(x) for x in input().split()]
    seqs = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = sequence_reconstruction(original, seqs)
    print("true" if res else "false")

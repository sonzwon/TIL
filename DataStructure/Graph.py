from collections import deque, defaultdict

# [ 너비 우선 탐색 : BFS (Breath First Search)]
def BFS(graph, start):
    result = []
    visited = set()
    queue = deque()
    queue.append(start)
    while queue:
        next_ = queue.popleft() 
        result.append(next_)
        for n in graph[next_]:
            if n not in visited:
                queue.append(next_)
                visited.add(next_)
    return result


# [ 깊이 우선 탐색 : DFS (Depth First Search)]
def DFS(graph, start):
    result = []
    visited = set()
    stack = []
    stack.append(start)
    while stack:
        next_ = stack.pop()
        result.append(next_)
        for n in graph[next_]:
            if n not in visited:
                visited.add(n)
                stack.append(n)
    return result
                
# [ BFS,DFS TEST ]
if __name__=='__main__':
    graph = defaultdict(list)
    graph[0].append(1)
    graph[1].append(2)
    graph[2].append(3)
    graph[3].append(4)
    graph[4].append(3)
    
    print(f"BFS(graph,0): {BFS(graph,0)}")
    print(f"DFS(graph,0): {DFS(graph,0)}")
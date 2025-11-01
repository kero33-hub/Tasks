n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = [1]
parent = [-1] * (n + 1)

for curr in queue:
    if curr == n:
        path = []
        while curr != -1:
            path.append(curr)
            curr = parent[curr]
        print(len(path))
        print(*path[::-1])
        exit()
    
    for next in graph[curr]:
        if parent[next] == -1 and next != 1:
            parent[next] = curr
            queue.append(next)

print("IMPOSSIBLE")
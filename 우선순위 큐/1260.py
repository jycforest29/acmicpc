import sys
from collections import deque

def dfs(adj, visited, v):
    visited[v] = True
    print(v, end = ' ')
    for i in adj[v]:
        if not visited[i]:
            dfs(adj, visited, i)

def bfs(adj, visited, deq):
    while len(deq) != 0:
        q = deq.popleft()
        print(q, end = ' ')
        for i in adj[q]:
            if not visited[i]:
                visited[i] = True
                deq.append(i)

n, m, v = map(int, sys.stdin.readline().split())
adj = [[] for i in range(n+1)]
for i in range(m):
    v1, v2 = map(int, sys.stdin.readline().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

for i in range(n+1):
    adj[i].sort()
    
visited1 = [False for i in range(n+1)]
dfs(adj, visited1, v)

print()

visited2 = [False for i in range(n+1)]
deq = deque([v])
visited2[v] = True
bfs(adj, visited2, deq)
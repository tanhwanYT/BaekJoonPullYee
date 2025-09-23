import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int,input().split())
nodelist = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    nodelist[a].append(b)
    nodelist[b].append(a)

def dfs(nodelist, startnode):
    visited[startnode] = True
    print(startnode, end = " ")
    for next in sorted(nodelist[startnode]):
        if(not visited[next]): dfs(nodelist, next)

def bfs(nodelist, startnode):
    queue.append(startnode)
    visited[startnode] = True
    while(queue):
        num = queue.popleft()
        print(num, end=" ")
        for next in sorted(nodelist[num]):
            if(not visited[next]):
                queue.append(next)
                visited[next] = True

for i in range(1, 1+n): nodelist[i].sort()

visited = [False] * (n+1)
dfs(nodelist, v)
visited = [False] * (n+1)
print()
queue = deque()
bfs(nodelist, v)
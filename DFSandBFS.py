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
    for i in range(m):
        if(nodelist[i] == nodelist):
            print(startnode, end = " ")
            bfs(nodelist, i)
        else:
            bfs(nodelist, i)

def bfs(nodelist, startnode):
    queue.append(startnode)
    visited[node] = True
    while(len(queue) == 0):
        num = pop.queue()
        print(pop.queue(), end=" ")
        for i in range(m):
            if(nodelist[num][i] == 1):
                queue.append(i)
                visited[i] = True

for i in range(1, 1+n): numlist[i].sort

visited = [False] * (n+1)
dfs(nodelist, v)
visited = [False] * (n+1)
print()
queue = deque()
bfs(nodelist, v)
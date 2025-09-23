import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int,input().split())
nodelist = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int,input().split())
    nodelist[u].append(v)
    nodelist[v].append(u)

def dfs(nodelist, pointlist, num, visited):
    if(num not in visited):
        visited.add(num)
        pointlist.append(num)
        nbr = set(nodelist[num]) - visited
        for j in nbr:
            dfs(nodelist, pointlist, j, visited) 
        return pointlist 

def findconnect(nodelist):
    visited = set()
    pointlist = []

    for i in range(1, len(nodelist)):
        if(i not in visited):
            point = dfs(nodelist, [], i, visited)
            pointlist.append(point)
    print(len(pointlist))

for i in range(1,n+1): nodelist[i].sort()

findconnect(nodelist)
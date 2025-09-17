import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split())
queue = []
index = []
cnt = 0

for i in range(1 ,n+1): queue.append(i)

while(len(queue) > 0):
    cnt = (cnt + k - 1) % len(queue)
    index.append(queue[cnt])
    del queue[cnt]

print("<" + ", ".join(map(str, index)) + ">")
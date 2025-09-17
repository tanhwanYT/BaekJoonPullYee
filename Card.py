import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque()

for i in range(1,n+1): queue.append(i)

while(1):
    if(len(queue) == 1):
        print(queue[0])
        break
    del queue[0]
    queue.append(queue[0])
    del queue[0]
import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()
for i in range(n):
    index = sys.stdin.readline().split()
    if(index[0] == "push"):
        queue.append(int(index[1]))
    elif(index[0] == "pop"):
        if(queue):
            print(queue[0])
            del queue[0]
        else:
            print(-1)
    elif(index[0] == "size"):
        print(len(queue))
    elif(index[0] == "empty"):
        if(queue): print(0)
        else: print(1)
    elif(index[0] == "front"):
        if(queue):
            print(queue[0])
        else:
            print(-1)       
    elif(index[0] == "back"):
        if(queue):
            print(queue[-1])
        else:
            print(-1)  

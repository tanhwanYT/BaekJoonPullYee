import sys
input = sys.stdin.readline

n = int(input())
stack = []
for i in range(n):
    order = list(map(str, input().split()))
    if(order[0] == "push"):
        stack.append(int(order[1]))
    elif(order[0] == "pop"):
        if(len(stack)==0):
            print(-1)
        else:
            print(stack[-1])
            del stack[-1]
            # remove는 오류남 왜인지 진짜 모름
    elif(order[0] == "size"):
        print(len(stack))
    elif(order[0] == "empty"):
        if(len(stack)==0):
            print(1)
        else:
            print(0)
    elif(order[0] == "top"):
        if(len(stack)==0):
            print(-1)
        else:
            print(stack[-1])
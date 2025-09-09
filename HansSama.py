import sys
input = sys.stdin.readline

X = int(input())

if(X > 99):
    cnt = 99
    for i in range(100,X+1):
        num = []
        minus = []
        while(i != 0):
            num.append(i%10)
            i=i//10
        for j in range(len(num)-1):
            minus.append(num[j+1] - num[j])
        if(minus.count(minus[0]) == len(minus)): cnt += 1 
    print(cnt)
else:
    print(X)
num = int(input())
for i in range(num):
    point =0
    OX = input().split("X")
    for j in OX:
        m = len(j)
        cnt=0
        for l in range(0,m):
            cnt = cnt + l + 1
        point += cnt
    print(point)
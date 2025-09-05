a = int(input())
for i in range(a):
    sum=0
    point = list(map(int, input().split()))
    cnt = point[0]
    for j in range(1,cnt+1):
        sum += point[j]
    ans = round(sum / cnt, 3)
    god=0
    for j in range(1,cnt+1):
        if(point[j] > ans):
            god += 1
    ans = round(god / cnt * 100, 3)
    print(f"{ans: .3f}%")
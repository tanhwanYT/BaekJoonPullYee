import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    s = int(input())
    cnt =0
    l = s//3
    for f in range(l):
        for j in range(1,3):
            for l in range(1,3):
                for k in range(1,3):
                    if((j+l+k) == s): cnt += 1
    print(cnt)

# 무한의 계단
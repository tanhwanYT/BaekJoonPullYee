import sys
import random
input = sys.stdin.readline
n = int(input())

num = [0] * n

for i in range(n):
    num[i] = int(input())

def quick_sort(num):
    if(len(num) <= 1): return num
    piv = random.choice(num)
    front, pivot, back = [],[],[]
    for i in num:
        if(i < num[piv]):
            front.append(i)
        elif(i > num[piv]):
            back.append(i)
        else:
            pivot.append(i)
    return quick_sort(front) + quick_sort(pivot) + quick_sort(back)

num = quick_sort(num)

sys.stdout.write("\n".join(map(str, num)))

#이거 오류남
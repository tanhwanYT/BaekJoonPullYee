import sys
input = sys.stdin.readline

n = int(input())
water = list(map(int, input().split()))

mincouple = [0,0]
minval = 2_000_000_001 # 10 * 18은 오류

def leejin(left, right):
    global minval
    total = left + right
    if(minval > abs(total)): 
        minval = abs(total)
        mincouple[0] = min(left, right)
        mincouple[1] = max(left, right)
    return total

water.sort()
lo = 0
hi = n-1

while(lo < hi):
    total = leejin(water[lo], water[hi])
    if(0 == total):
        break
    elif(0 < total):
        hi -= 1
    else:
        lo += 1
        
print(mincouple[0], mincouple[1])

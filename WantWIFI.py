import sys
input = sys.stdin.readline

n, m = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

def canInstall(distance):
    count = 1
    last = house[0]

    for i in range(1, n):
        if house[i] - last >= distance:
            count += 1
            last = house[i]
    return count >= m

lo, hi = 1, house[-1] - house[0]
result = 0

while lo <= hi:
    mid = (lo + hi) // 2
    if canInstall(mid):
        result = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(result)


# def NoKTandSKT(house, m, mi):
#     s= (max(house)-mi) // m
#     h = max(house)
#     l=mi
#     mid = (h+l)//2
#     while(l <= h):
#         if(abs(h - l) == s):
#             return abs(h - l) 
#         elif(abs(h - l) > s): l = mid
#         elif(abs(h - l) < s): h = mid +1
#         mid = (h+l)//2
#     return abs(h - l)
# house = sorted(house)
# arr = []
# mi = 0
# for i in range(m):
#     arr.append(NoKTandSKT(house,m,mi))
#     m-=1
#     mi = arr[i]
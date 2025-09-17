import sys
import heapq
input = sys.stdin.readline

n= int(input())
heap = []

for i in range(n):
    num = int(input())
    if(num == 0):
        if(heap):
            max = heapq.nlargest(1, heap, key = many)
            print(max)
            heapq.heappop(heapq.nlargest(1, heap))
        else:
            print("[0]")
    else:
        heapq.heappush(heap, num)

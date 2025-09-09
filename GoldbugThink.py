import math
from itertools import product
import sys
input = sys.stdin.readline

a = int(input())
prime = [0]
def primenum(x):
    arr = [i for i in range(x+1)]
    end = int(x**(1/2))
    for i in range(2, end+1):
        if arr[i] == 0: 
            continue
        for j in range(i*i, x+1, i): 
            arr[j] = 0
            
    return [i for i in arr[2:] if arr[i]]

for i in range(a):
    num = int(input())
    prime = []
    prime = primenum(num)

    left = 0
    right = len(prime)-1
    best = (0,0)
    maxa = 10000001
    while left <= right:
        s = prime[left] + prime[right]
        if s == num:          
            if(maxa >= abs(prime[left] - prime[right])):
                best = (prime[left], prime[right])
                maxa = abs(prime[left] - prime[right])
                left += 1
        elif s < num:
            left += 1
        else:
            right -= 1

    sys.stdout.write(" ".join(map(str, best)) + "\n")

    # realS = list(product(prime, repeat=2))
    # maxa = 10000001
    # ans = [0] * 2

    # for j in realS:
    #     if(sum(j)==num):
    #         if(maxa >= abs(j[1] - j[0])):
    #             ans = j
    #             maxa = abs(j[1] - j[0])


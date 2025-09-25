import sys
input = sys.stdin.readline

n =int(input())
num = [1,1]

for i in range(1,n):
    num.append((num[i-1] + num[i])%15746)

print(num[n] % 15746)

# 1, 00으로 만들수있는 조합 구하기
# 00을 미리 박아두고 1넣어보기 배열을 만들어서 append로 넣어주고 배열은 0,1,2,3 계속 돌면서 00을 받고
# 대충 숫자보니 피보나치수열이라 메모이제이션써서 풀기로함
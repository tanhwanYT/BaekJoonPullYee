import sys
input = sys.stdin.readline

n = int(input())
word = [''] * n
for i in range(n):
    word[i] = str(input())

word = set(word)
word = sorted(list(word))
word.sort(key=len)
# length = [len(i) for w in word] 배열 길이순으로 정렬
# word = sorted(range(len(word)), key = lambda k : word[k]) 

for i in word:
    sys.stdout.write("".join(map(str, i)))
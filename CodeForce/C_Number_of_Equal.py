from collections import Counter

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

A = Counter(a)
B = Counter(b)

ans = 0
for x in A:
    if x in B:
        ans += A[x] * B[x]

print(ans)

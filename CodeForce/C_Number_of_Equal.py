n, m = map(int, input().split())

a = [int(x) for x in input().split()]

b = [int(x) for x in input().split()]

i = j = 0
ans = 0

while i < n and j < m:
    if a[i] == b[j]:
        t = j
        while t < m and b[t] == b[j]:
            ans += 1
            t += 1
        i += 1
    elif a[i] < b[j]:
        i += 1
    else:
        j += 1

print(ans)

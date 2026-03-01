n, k = map(int, input().split())
arr = [int(x) for x in input().split()]

idx = []

for i in range(n):
    idx.append((arr[i], i+1))

idx.sort()
count = 0
res = []

for day, i in idx:
    if k >= day:
        count += 1
        k -= day
        res.append(i)
    else:
        break


if count > 0:
    print(count)
    print(*res)
else:
    print(0)

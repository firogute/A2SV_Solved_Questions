from collections import Counter

n = int(input())

for _ in range(n):
    s = input()

    ctr = Counter(s)

    count = 0

    for value in ctr.values():
        if value >= 2:
            count += 1

    if count > 1:
        print("YES")
    else:
        print("NO")

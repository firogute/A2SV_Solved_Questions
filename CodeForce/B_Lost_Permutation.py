t = int(input())
for _ in range(t):
    m, s = map(int, input().split())
    b = list(map(int, input().split()))

    used = set(b)
    mx = max(b)

    x = 1
    while s > 0:
        if x not in used:
            s -= x
            used.add(x)
        x += 1

    if s < 0:
        print("NO")
        continue

    new_max = max(used)

    ok = True
    for v in range(1, new_max + 1):
        if v not in used:
            ok = False
            break

    print("YES" if ok else "NO")

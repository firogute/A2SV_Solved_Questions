t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    seen = {}
    ok = False

    for i in range(n - 1):
        pair = s[i:i+2]
        if pair in seen:
            if i - seen[pair] >= 2:
                ok = True
                break
        else:
            seen[pair] = i

    print("YES" if ok else "NO")

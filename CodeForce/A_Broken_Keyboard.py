n = int(input())

for _ in range(n):
    s = input()

    visited = set()

    i = 0
    while i < len(s):
        if i + 1 < len(s) and s[i] == s[i+1]:
            i += 2
        else:
            visited.add(s[i])
            i += 1

    res = sorted(list(visited))
    print("".join(res))

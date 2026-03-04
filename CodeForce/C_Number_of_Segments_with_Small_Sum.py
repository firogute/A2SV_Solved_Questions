
n, s = map(int, input().split())
a = list(map(int, input().split()))

l = 0
window_sum = 0
ans = 0

for r in range(n):
    window_sum += a[r]

    while window_sum > s:
        window_sum -= a[l]
        l += 1

    ans += (r - l + 1)

print(ans)

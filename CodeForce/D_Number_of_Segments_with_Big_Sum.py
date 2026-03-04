n, s = map(int, input().split())
a = list(map(int, input().split()))

r = 0
window_sum = 0
ans = 0

for l in range(n):

    while r < n and window_sum < s:
        window_sum += a[r]
        r += 1

    if window_sum >= s:
        ans += (n - r + 1)

    window_sum -= a[l]

print(ans)

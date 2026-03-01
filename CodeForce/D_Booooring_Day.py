t = int(input())

for _ in range(t):
    n, l, r = map(int, input().split())
    arr = [int(x) for x in input().split()]

    left = 0
    count = 0

    curr_sum = 0

    for right in range(n):
        curr_sum += arr[right]

        while curr_sum > r and left <= right:
            curr_sum -= arr[left]
            left += 1

        if l <= curr_sum <= r:
            count += 1
            curr_sum = 0
            left = right + 1

    print(count)

n = int(input())

for _ in range(n):
    t = int(input())
    arr = [int(x) for x in input().split()]

    arr.sort(reverse=True)

    i = 0
    max_score = 0

    while i < 2*t:
        max_score += min(arr[i], arr[i+1])

        i += 2

    print(max_score)

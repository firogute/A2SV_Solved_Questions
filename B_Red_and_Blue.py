t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    max_red = 0
    curr = 0
    for x in r:
        curr += x
        max_red = max(max_red, curr)

    # print(max_red)

    max_blue = 0
    curr = 0
    for x in b:
        curr += x
        max_blue = max(max_blue, curr)

    print(max_red + max_blue)

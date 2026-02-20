def rotate90(g):
    n = len(g)
    
    return [[g[n-1-c][r] for c in range(n)] for r in range(n)]


t = int(input())

for _ in range(t):
    n = int(input())
    grid = [list(input().strip()) for _ in range(n)]

    R0 = grid
    R90 = rotate90(R0)
    R180 = rotate90(R90)
    R270 = rotate90(R180)

    total_cost = 0

    for r in range(n):
        for c in range(n):

            vals = [
                R0[r][c],
                R90[r][c],
                R180[r][c],
                R270[r][c]
            ]

            ones = vals.count('1')
            zeros = 4 - ones

            total_cost += min(ones, zeros)

    print(total_cost // 4)

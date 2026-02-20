n = int(input())

contests = list(map(int, input().split()))

contests.sort()

problem = 1
day = 0

for problems in contests:
    if problem <= problems:
        day += 1
        problem += 1

print(day)

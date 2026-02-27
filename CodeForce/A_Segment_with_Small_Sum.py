n, s = map(int, input().split())

arr = [int(x) for x in input().split()]

left = 0
max_sum = 0
for num in arr:
    max_sum += num
    
    if max_sum =
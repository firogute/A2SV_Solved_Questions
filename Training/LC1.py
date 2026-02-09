n = int(input())
arr = list(map(int, input().split()))

arr.sort()

count = arr.count(arr[-1])

print(arr[n-count-1])

    

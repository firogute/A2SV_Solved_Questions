intervals = [[1,4],[0,4]]
res = []
n = len(intervals)

new = sorted(intervals, key = lambda x: x[0])
i = 0
while i < n:
    if i+1 < n and new[i+1][0] <= new[i][1]:
        res.append([new[i][0], new[i+1][1]])
        i +=1
    else:
        res.append([new[i][0], new[i][1]])
    i+=1

print(res)
    

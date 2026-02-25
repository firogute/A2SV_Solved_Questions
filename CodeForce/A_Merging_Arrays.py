x, y = list(map(int, input().split()))

lst1 = [int(x) for x in input().split()]
lst2 = [int(x) for x in input().split()]
res = []

ptr1, ptr2 = 0, 0

while ptr1 < len(lst1) and ptr2 < len(lst2):
    if lst1[ptr1] <= lst2[ptr2]:
        ele = lst1[ptr1]
        ptr1 += 1
    else:
        ele = lst2[ptr2]
        ptr2 += 1
    res.append(ele)

res.extend(lst1[ptr1:])
res.extend(lst2[ptr2:])


print(*res)

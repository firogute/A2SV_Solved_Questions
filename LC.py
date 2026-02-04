x = int(input())
y = int(input())
z = int(input())
n = int(input())


lst = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]

new_lst = [x for x in lst if x[0]+x[1]+x[2] != n ]

print(new_lst)

t = int(input())
for _ in range(t):
    n = int(input())

    Aw = 0  
    Ab = 0  
    Bw = 0  
    Bb = 0  

    step = 1
    turn = "Alice"  
    used = 0
    limit = 1  

    pos = 0  

    while pos < n:
        take = step
        if pos + take > n:
            take = n - pos 

        for k in range(take):
            
            if (pos + k) % 2 == 0:
                color = "white"
            else:
                color = "black"

            if turn == "Alice":
                if color == "white":
                    Aw += 1
                else:
                    Ab += 1
            else:
                if color == "white":
                    Bw += 1
                else:
                    Bb += 1

        pos += take
        step += 1

        used += 1
        if used == limit:
            if turn == "Alice":
                turn = "Bob"
            else:
                turn = "Alice"
            used = 0
            limit = 2 

    print(Aw, Ab, Bw, Bb)

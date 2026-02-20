t = int(input())
for _ in range(t):
    n = int(input())
    alice = 0
    bob = 0

    step = 1
    turn = "alice"
    used = 0
    limit = 1  

    while n > 0:
        take = step if step <= n else n

        if turn == "alice":
            alice += take
        else:
            bob += take

        n -= take
        step += 1

        used += 1
        if used == limit:
            if turn == "alice":
                turn = "bob"
            else:
                turn = "alice"

            used = 0
            limit = 2  

    print(alice, bob)

t = int(input())

for _ in range(t):
    n, x, k = map(int, input().split())
    commands = input()

    zeros = 0
    command_tracker = 0
    move = {"L": -1, "R": 1}

    for _ in range(k):

        if command_tracker >= len(commands):
            break

        x += move[commands[command_tracker]]

        if x == 0:
            command_tracker = 0
            zeros += 1
        else:
            command_tracker += 1

    print(zeros)

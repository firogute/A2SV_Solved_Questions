t = int(input())

for _ in range(t):
    s = input().strip()

    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 2   

    n = 2 * len(s)
    res = [""] * n

    left = 0
    right = n - 1

    for char in freq:
        while freq[char] > 0:
            res[left] = char
            res[right] = char
            left += 1
            right -= 1
            freq[char] -= 2

    print("".join(res))

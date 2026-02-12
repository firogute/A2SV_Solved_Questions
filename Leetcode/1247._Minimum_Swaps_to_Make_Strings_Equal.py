class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        mis_x = 0
        mis_y = 0

        for a, b in zip(s1, s2):
            if a != b:
                if a == 'x':
                    mis_x += 1
                else:
                    mis_y += 1

        if (mis_x + mis_y) % 2 == 1:
            return -1

        return mis_x // 2 + mis_y // 2 + (mis_x % 2) * 2

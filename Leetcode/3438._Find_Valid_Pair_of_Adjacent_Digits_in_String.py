from collections import Counter


class Solution:
    def findValidPair(self, s: str) -> str:
        ctr = Counter(s)

        for i in range(len(s) - 1):
            a = s[i]
            b = s[i + 1]

            if a != b and int(a) == ctr[a] and int(b) == ctr[b]:
                return a + b

        return ""

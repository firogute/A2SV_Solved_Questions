from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_ctr = Counter(s)
        t_ctr = Counter(t)

        diff = t_ctr - s_ctr

        return sum(diff.values())

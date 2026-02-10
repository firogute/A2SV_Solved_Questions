class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False

        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t

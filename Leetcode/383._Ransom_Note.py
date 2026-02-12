from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        count = Counter(magazine)

        for s in ransomNote:
            print(count)
            if s not in count:
                return False
            elif s in magazine:
                count[s] -= 1
                if count[s] == 0:
                    del count[s]

        return True

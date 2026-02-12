from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        if set(word1) != set(word2):
            return False

        word_1 = Counter(word1)
        word_2 = Counter(word2)

        return sorted(word_1.values()) == sorted(word_2.values())

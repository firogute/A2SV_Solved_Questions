from collections import Counter
import math


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        freq = Counter(nums)
        # dominant_check = n/2

        dominant_ele = max(freq.keys(), key=lambda x: freq[x])

        total_count = freq[dominant_ele]

        left_count = 0

        for i, num in enumerate(nums):
            if num == dominant_ele:
                left_count += 1

            if left_count * 2 > (i + 1) and (total_count - left_count) * 2 > (n-i + 1):
                return i

        return -1

        # print(dominant_ele)

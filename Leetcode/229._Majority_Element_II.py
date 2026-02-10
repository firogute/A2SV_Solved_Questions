from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        ctr = Counter(nums)
        min_freq = (len(nums) // 3) + 1

        for ele, freq in ctr.items():
            if freq >= min_freq:
                res.append(ele)

        return res

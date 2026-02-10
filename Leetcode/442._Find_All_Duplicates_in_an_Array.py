from collections import Counter


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        counter = Counter(nums)

        for num, count in counter.items():
            if counter[num] == 2:
                res.append(num)

        return res

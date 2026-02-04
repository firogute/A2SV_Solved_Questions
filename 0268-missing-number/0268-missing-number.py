class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        big = len(nums)

        for i in range(big+1):
            if i not in nums:
                return i
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = list(enumerate(nums))
        temp.sort(key=lambda x: x[1])

        res = [0] * len(nums)

        count = 0

        for i in range(len(nums)):
            if i > 0 and temp[i][1] != temp[i-1][1]:
                count = i
            res[temp[i][0]] = count

        return res

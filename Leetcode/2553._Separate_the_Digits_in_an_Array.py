class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        output = []
        res = []

        num_str = [str(x) for x in nums]

        for s in num_str:
            res.extend(list(s))

        return [int(x) for x in res]

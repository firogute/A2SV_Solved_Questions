class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))

        nums_str.sort(key=lambda a: a*10, reverse=True)
        print(nums_str)

        result = "".join(nums_str)
        return "0" if result[0] == "0" else result

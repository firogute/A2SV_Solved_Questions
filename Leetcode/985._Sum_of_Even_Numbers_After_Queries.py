class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        output = []
        temp_sum = 0
        for num in nums:
            if num % 2 == 0:
                temp_sum += num
        print(temp_sum)

        for val, index in queries:
            temp = nums[index]
            nums[index] = nums[index] + val
            # print(nums)
            if temp % 2 != 0:
                if nums[index] % 2 == 0:
                    temp_sum += nums[index]
            else:
                if nums[index] % 2 == 0:
                    temp_sum += val
                else:
                    temp_sum -= temp
            # print(temp_sum)
            output.append(temp_sum)
            # print(output)

        return output

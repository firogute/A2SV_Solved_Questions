class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # n = False
        # for i in range(len(nums)-2):
        #     if nums[i] < nums[i+2] < nums[i+1]:
        #         n = True

        # return n

        stack = []

        curMin = nums[0]

        for n in nums[1:]:
            while stack and n >= stack[-1][0]:
                stack.pop()

            if stack and n< stack[-1][0] and n> stack[-1][1]:
                return True

            stack.append([n,curMin])

            curMin = min(n,curMin)

            print(curMin)

        return False
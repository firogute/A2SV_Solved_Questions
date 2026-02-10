class Solution:
    def sumOfThree(self, num: int) -> List[int]:

        # 1. First approach time limit exceeded

        # output = []
        # for i in range(1, num-3):
        #     temp = i + (i+1) + (i +2)

        #     if temp == num:
        #         output.extend([i, i+1, i+2])
        #         return output
        # return []

        # 2nd approach

        if (num - 3) % 3 != 0:
            return []

        x = (num - 3) // 3

        return [x, x+1, x+2]

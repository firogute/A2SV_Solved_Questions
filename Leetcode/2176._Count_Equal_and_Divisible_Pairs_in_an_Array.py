class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        indexes = sorted(list(enumerate(nums)) , key = lambda x : x[1])
        i , j = 0, 1
        output = 0
        # print(indexes)
        while j < len(indexes):
            # print(indexes[i], indexes[j])
            # print(output)
            if indexes[i][1] != indexes[j][1]:
                i += 1
                j += 1
            else:
                while j < len(indexes) and indexes[i][1] == indexes[j][1]:
                    divisible = ((indexes[i][0] * indexes[j][0]) % k == 0)
                    print(divisible)
                    if divisible:
                        output += 1
                    j +=1
                i += 1
                j = i + 1

        # print(output)
        return output



        
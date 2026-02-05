class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        out = [list1[0]]
        minimum_sum = float("inf")
        for x in enumerate(list1):
            for y in enumerate(list2):
                index_sum = x[0] + y[0]
                if x[1] == y[1] and index_sum < minimum_sum:
                     minimum_sum = index_sum
                     out[-1] = x[1]
                elif x[1] == y[1] and index_sum == minimum_sum:
                    out.append(x[1])
        return out

                



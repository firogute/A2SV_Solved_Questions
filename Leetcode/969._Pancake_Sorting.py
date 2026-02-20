class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)

        for curr in range(n, 1, -1):
            i = arr.index(curr)

            if i == curr - 1:
                continue

            if i != 0:
                res.append(i + 1)
                arr[:i+1] = reversed(arr[:i+1])

            res.append(curr)
            arr[:curr] = reversed(arr[:curr])

        return res

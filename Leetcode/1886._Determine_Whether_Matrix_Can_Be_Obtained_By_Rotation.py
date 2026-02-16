class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        def rotate90(a):
            n = len(a)
            new = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    new[i][j] = a[n - j - 1][i]
            return new

        for _ in range(4):
            if mat == target:
                return True
            mat = rotate90(mat)

        return False

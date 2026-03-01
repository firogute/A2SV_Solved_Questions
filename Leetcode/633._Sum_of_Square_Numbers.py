class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = 0

        while b*b <= c:
            b += 1
        b -= 1

        while a <= b:
            s = a*a + b*b
            if s == c:
                return True
            elif s > c:
                b -= 1
            else:
                a += 1

        return False

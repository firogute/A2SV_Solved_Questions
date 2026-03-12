class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # op = "("
        # cl = ")"
        # char = list(s)
        # print(char)

        # return char.count(")")

        score = 0
        stack = []
        for par in s:
            if par == "(":
                stack.append(score)
                score = 0
            else:
                score = stack.pop() + max(2*score, 1)

        return score

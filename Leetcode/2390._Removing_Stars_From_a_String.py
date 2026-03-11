class Solution:
    def removeStars(self, s: str) -> str:

        # One solution but not efficient
        # stack = list(s)

        # while "*" in stack:
        #     stack.pop(stack.index("*")-1)
        #     stack.pop(stack.index("*"))

        # return ''.join(stack)

        stack = []
        for e in s:
            if e == "*":
                stack.pop()
            else:
                stack.append(e)

        return "".join(stack)

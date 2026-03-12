class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                temp = []
                while stack and stack[-1] != "[":
                    temp.append(stack.pop())

                temp = "".join(reversed(temp))
                # print(temp)
                if stack:
                    stack.pop()

                freq = ""
                while stack and '0' <= stack[-1] <= '9':
                    freq += stack.pop()

                freq = int(freq[::-1])

                # print(int(freq), temp)
                # print(stack)

                for _ in range(freq):
                    stack.append(temp)
        return "".join(stack)

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        string_list = s.split()

        if len(pattern) != len(string_list):
            return False

        # print(string_list)

        temp = {}

        for i, char in enumerate(pattern):
            if char not in temp:
                if string_list[i] not in temp.values():
                    # print(list(temp.values()))
                    temp[char] = string_list[i]
                else:
                    return False
            else:
                if temp[char] != string_list[i]:
                    return False
        return True

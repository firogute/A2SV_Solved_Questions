class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anagrams = {}

        for i, ele in enumerate(strs):
            s = ''.join(sorted(ele))
            if s in anagrams:
                anagrams[s].append(i)
            else:
                anagrams[s] = [i]

        for key, value in anagrams.items():
            r = []
            for i in value:
                r.append(strs[i])

            res.append(r)

        return res

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        chemo = 0
        l, r = 0, len(skill) - 1
        prev = skill[l] + skill[r]
        while l < r:
            current = skill[l] + skill[r]
            if current != prev:
                return -1
            else:
                chemo += skill[l] * skill[r]
                prev = current
            r -= 1
            l += 1

        return chemo

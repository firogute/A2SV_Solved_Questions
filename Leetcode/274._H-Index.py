class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        max_h = 0

        for i in range(len(citations)):
            if citations[i] >= i + 1:
                max_h = i + 1
            else:
                break

        return max_h

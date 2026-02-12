from collections import Counter


class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        counter = Counter()

        for resp in responses:
            seen = set()
            for r in resp:
                if r not in seen:
                    counter[r] += 1
                    seen.add(r)

        max_freq = max(counter.values())

        return min(k for k, v in counter.items() if v == max_freq)

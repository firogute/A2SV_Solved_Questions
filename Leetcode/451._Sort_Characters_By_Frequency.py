from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)

        sorted_items_asc = sorted(
            count.items(), key=lambda item: item[1], reverse=True)

        sorted_dict_asc = dict(sorted_items_asc)

        res = ""

        for ele, freq in sorted_dict_asc.items():
            res += ele * freq

        return res

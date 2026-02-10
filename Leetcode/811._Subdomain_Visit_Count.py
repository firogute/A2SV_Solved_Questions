class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = {}
        res = []

        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)

            parts = domain.split(".")

            for i in range(len(parts)):
                sub = ".".join(parts[i:])
                counts[sub] = counts.get(sub, 0) + count
        for domain, count in counts.items():
            res.append(str(count) + " " + domain)

        return res

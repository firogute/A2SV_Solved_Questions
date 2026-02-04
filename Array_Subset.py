# User function Template for python3

class Solution:
    # Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        count_a = {}
        for elem in a:
            if elem not in count_a:
                count_a[elem] = 1
            else:
                count_a[elem] += 1

        for elem in b:
            if elem not in count_a or count_a[elem] == 0:
                return False
            else:
                count_a[elem] -= 1

        return True

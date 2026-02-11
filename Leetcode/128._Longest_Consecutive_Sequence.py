class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums) # to remove duplicates

        longest = 0 #for tracking the longest consecutive sequence count

       
        for num in s:

            # check if the number is the starting number [6,5,4,3] 6 is not starting number so we have to go to 3
            if num - 1 not in s:   
                length = 1
                nxt = num + 1

                while nxt in s:

                    length += 1
                    nxt += 1

                longest = max(longest, length) #to update the longest consecutive sequence

        return longest
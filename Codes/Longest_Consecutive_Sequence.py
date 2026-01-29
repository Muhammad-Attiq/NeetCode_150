# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

class Solution(object):
    def longestConsecutive(self, nums):

        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                streak = 1
                next_num = num + 1
            
                while next_num in num_set:
                    streak += 1 
                    next_num += 1

                longest = max(longest, streak)

        return longest

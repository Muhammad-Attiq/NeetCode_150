# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
class Solution(object):
    def twoSum(self, nums, target):
        i = 0
        j = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return i, j
        return None 

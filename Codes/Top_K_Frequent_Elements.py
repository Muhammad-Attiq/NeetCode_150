# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        sorted_num = sorted(count, key = lambda x : count[x], reverse = True)

        return sorted_num[:k]

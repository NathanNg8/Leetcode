class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {}
        for i in nums:
            seen[i] = 1 
        count = 1
        while True:
            if count not in seen:
                return count
            count += 1 
        
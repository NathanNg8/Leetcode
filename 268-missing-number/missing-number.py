class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {}
        for i in nums:
            if i not in seen:
                seen[i] = 1
        
        for j in range(len(nums)+1):
            if j not in seen:
                return j 

        
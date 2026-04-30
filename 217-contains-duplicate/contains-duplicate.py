class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = {}
        for number in nums:
            if number in seen:
                return True
            seen[number] = 1 
        return False        
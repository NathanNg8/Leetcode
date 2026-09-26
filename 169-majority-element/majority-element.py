class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        counts = Counter(nums)
        distinct_count = len(nums)
        most_frequent_num, frequency = counts.most_common(1)[0]
        return most_frequent_num
            







        
            
        
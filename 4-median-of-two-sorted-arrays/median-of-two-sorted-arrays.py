class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        arr = nums1 + nums2
        arr.sort()
        count = len(arr)
        median = 0 
        if count % 2 == 0:
            median = (arr[(count//2 - 1)] + arr[count//2]) / 2.0
        else:
            median = arr[int(count//2)]

        return median
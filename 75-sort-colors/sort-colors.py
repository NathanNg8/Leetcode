class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def quicksort(left, right):
            if left >= right:
                return

            pivot = nums[right]
            i = left

            for j in range(left, right):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1

            nums[i], nums[right] = nums[right], nums[i]

            quicksort(left, i - 1)
            quicksort(i + 1, right)

        quicksort(0, len(nums) - 1)
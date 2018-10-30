class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            if i == 0:
                if nums[i] > nums[i+1]:
                    return i
            if i == len(nums)-1:
                if nums[i] > nums[i-1]:
                    return i
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
        
        
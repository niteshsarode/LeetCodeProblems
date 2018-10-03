class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        length = 1
        isPositive = True
        for i in range(0, len(nums)-1):
            if length == 1:
                if nums[i] < nums[i+1]:
                    isPositive = True
                elif nums[i] > nums[i+1]:
                    isPositive = False
            if isPositive and nums[i] < nums[i+1]:
                length += 1
                isPositive = False
            elif not isPositive and nums[i] > nums[i+1]:
                length += 1
                isPositive = True
        return length
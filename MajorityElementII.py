class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nby3 = len(nums) / 3
        print nby3
        result = []
        for num in nums:
            if num not in result:
                if nums.count(num) > nby3:
                    result.append(num)
        return result
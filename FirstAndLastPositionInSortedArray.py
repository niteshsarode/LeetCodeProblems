class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        flag = 0
        pos = [-1,-1] 
        for key, value in enumerate(nums):
            if value == target:
                if flag == 0:
                    pos[0] = key
                    pos[1] = key
                    flag = 1
                else:
                    pos[1] = key
        return pos
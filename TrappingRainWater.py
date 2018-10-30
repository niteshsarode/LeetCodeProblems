class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        l = len(height)
        left = [0] * l
        left[0] = height[0]
        right = [0] * l
        right[-1] = height[-1]
        sum = 0
        for i in range(1,l):
            left[i] = max(left[i-1],height[i])
        for i in range(l-2,-1,-1):
            right[i] = max(right[i+1],height[i])
        for i in range(1,l-1):
            sum += min(left[i],right[i]) - height[i]
        return sum
        
        
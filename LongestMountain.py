class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        isDown = False
        isUp = False
        upDown = False
        maxLength = 0
        length = 1
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                if isDown:
                    length = 2
                    isDown = False
                    isUp = True
                else:
                    length += 1
                    isUp = True
            elif A[i] < A[i-1] and isUp:
                length += 1
                isDown = True
                upDown = True
            elif A[i] == A[i-1]:
                length = 1
                isUp = False
            maxLength = max(maxLength, length)
        if maxLength == 1 or not upDown:
            return 0
        return maxLength
            
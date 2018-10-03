class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        for i in range(0,len(matrix)):
            if target <= matrix[i][len(matrix[i])-1]:
                for j in range(0,len(matrix[i])):
                    if matrix[i][j] == target:
                        return True
        return False
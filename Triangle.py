class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        minSum = 0
        lastRow = triangle[-1]
        
        for row in reversed(triangle[:-1]):
            tempRow = row[:]
            for i in range(0,len(row)):
                tempRow[i] += min(lastRow[i], lastRow[i+1])
            lastRow = tempRow                        
        return lastRow[0]
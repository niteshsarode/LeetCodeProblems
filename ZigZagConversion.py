class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        diff = numRows+numRows-3
        s = list(s)
        result = [""] * numRows
        goingDown = False
        curRow = 0
        
        if not s:
            return str("")
        
        if numRows == 1:
            return "".join(s)
                                  
        for char in s:
            result[curRow] += (char)
            if (curRow == 0 or curRow == numRows - 1):
                goingDown = not goingDown
            if goingDown:
                curRow += 1
            else:
                curRow -= 1

        ret = []
        for row in result:
            ret += row;
        return "".join(ret)
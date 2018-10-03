class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        numsDict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        if not digits:
            return result
        if len(digits) == 1:
            return list(numsDict[digits[0]])
        result = list(numsDict[digits[0]])
        for z in range(1,len(digits)):
            result = [x+y for x in result for y in numsDict[digits[z]]]
        return result
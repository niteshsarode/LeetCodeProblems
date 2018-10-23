class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sNums = sorted(nums)
        print len(sNums)
        length = len(sNums)
        if len(sNums) % 2 != 0:
            length = len(sNums) - 1
        for x in range(0,length,2):
            print x
            if sNums[x] != sNums[x+1]:
                return sNums[x]
        return sNums[len(sNums)-1]
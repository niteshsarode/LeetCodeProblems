class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        m = n
        count = 0
        while(True):
            if count > 5:
                return False
            count+=1
            arrN = list(str(n))
            print(arrN)
            sum = 0
            for i in arrN:
                sum += int(i)*int(i)
            if sum == 1:
                return True
            else:
                n = sum
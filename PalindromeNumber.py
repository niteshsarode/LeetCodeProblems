class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = str(x)
        if x < 0:
            return False
        if y == y[::-1]:
            return True
        else:
            return False
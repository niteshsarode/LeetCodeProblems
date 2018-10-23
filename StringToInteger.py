class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        num = str.strip()     
        reg = re.compile("(^[\+\-]?[0]?\d+)\D*")
        num = reg.findall(num)
        if not num:
            return 0
        output = "".join(num)
        result = int(output)
        limit = pow(2,31)
        result = max(result,-limit)
        result = min(result,limit-1)
        return result
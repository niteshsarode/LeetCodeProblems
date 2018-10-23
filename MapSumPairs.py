class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.map[key] = val            
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        sum = 0
        for k in self.map.keys():
            if k[0:len(prefix)] == prefix:
                sum += self.map[k]
        return sum

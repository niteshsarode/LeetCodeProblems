class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.c = capacity
        self.queue = [None] * capacity
        self.dict = {}
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            self.queue.remove(key)
            self.queue.append(key)
            return self.dict[key]
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dict:
            self.queue.remove(key)
            self.queue.append(key)
            self.dict[key] = value
            return
        else:
            if None not in self.queue:
                del self.dict[self.queue[0]]
            self.queue.pop(0)
            self.queue.append(key)
            self.dict[key]  = value
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
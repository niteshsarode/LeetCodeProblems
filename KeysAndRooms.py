class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        stack = [x for x in rooms[0]]
        orooms = [x for x in rooms[0]]
        while(stack):
            key = stack.pop()
            for i in rooms[key]:
                if i not in orooms:
                    stack.append(i)
                    orooms.append(i)
        for r in range(1,len(rooms)):
            if r not in orooms:
                return False
        return True
        
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = head
        count = 0
        while temp is not None:
            count = count + 1
            temp = temp.next
        temp = head
        numb = count - n
        if numb != 0:
            while numb != 0:
                numb = numb - 1
                prev = temp
                temp = temp.next
            prev.next = temp.next
        elif count > 1:
            head = head.next
        else:
            return None
        return head
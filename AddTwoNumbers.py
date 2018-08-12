# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Example:

#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = l1;
        num2 = l2;
        no1 = 0;
        no2 = 0;
        
        count = 0;
        while num1:
            if count > 0:
                no1 = num1.val*(10**count) + no1
            else:
                no1 = num1.val
            num1 = num1.next
            count = count + 1
        
        count = 0;
        while num2:
            if count > 0:
                no2 = num2.val*(10**count) + no2
            else:
                no2 = num2.val
            num2 = num2.next
            count = count + 1
            
        sum = no1 + no2;
        
        no3 = list(str(sum))
        no3.reverse()
        
        print no3
        
        for i in range(len(no3)):
            temp = ListNode(no3[i])
            if i == 0:
                l3 = temp
                head = temp
            else:
                l3.next = temp
                l3 = l3.next
            
        return head
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2

        if not l2:
            return l1

        result = ListNode(0, None)
        curr = result
        carry = 0
        while l1 or l2 or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0
            
            value = digit1 + digit2 + carry 
            digit = value % 10
            carry = value // 10

            nextNode = ListNode(digit, None)
            curr.next = nextNode
            curr = curr.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
    
        return result.next
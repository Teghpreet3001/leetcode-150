# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        #Push all the lists to a priority queue with priority as val 
        pqueue = []
        for index, linkedList in enumerate(lists):
            if linkedList:
                heapq.heappush(pqueue, (linkedList.val, linkedList, index))

        #Result Node
        result = ListNode(0, None)
        curr = result

        #Keep popping from the PQ and add them to curr.next
        while pqueue:
            poppedVal, poppedList, listIndex  = heapq.heappop(pqueue)
            newNode = ListNode(poppedVal, None)
            curr.next = newNode
            curr = curr.next

            #after every list popped, we want to put the next list in the PQ with index + 1 (topmost priority)
            if poppedList.next is not None:
                heapq.heappush(pqueue, (poppedList.next.val, poppedList.next, listIndex + 1))
        return result.next

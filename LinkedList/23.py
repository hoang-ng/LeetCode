# 23. Merge k Sorted Lists

# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

from Queue import PriorityQueue

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists1(self, lists):
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        for node in lists:
            if node: q.put((node.val,node))
        while q.qsize()>0:
            curr.next = q.get()[1]
            curr=curr.next
            if curr.next: q.put((curr.next.val, curr.next))
        return dummy.next

    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        
        first = lists[0]
        for i in range(1, len(lists)):
            first = self.mergeList(first, lists[i])
        return first
            
        
    def mergeList(self, l1, l2):
        dummy = current = ListNode(0)
        n1 = l1
        n2 = l2
        while n1 and n2:
            if n1.val < n2.val:
                current.next = n1
                n1 = n1.next
            else:
                current.next = n2
                n2 = n2.next
            current = current.next
        if n1:
            current.next = n1
        if n2:
            current.next = n2
        return dummy.next
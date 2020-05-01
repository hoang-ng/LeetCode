# 19. Remove Nth Node From End of List

# Given a linked list, remove the n-th node from the end of list and return its head.

# Example:
# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.

# Note:
# Given n will always be valid.

# Follow up:
# Could you do this in one pass?

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        current = head
        count = 0
        while current != None:
            count += 1
            current = current.next
        index = count - n
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        
        curr_index = 0
        while curr_index != index:
            prev = current
            current = current.next
            curr_index += 1
        prev.next = current.next
        
        return dummy.next

def removeNthFromEnd2(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        
        i = 0
        while i <= n:
            first = first.next
            i += 1
        
        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        
        return dummy.next
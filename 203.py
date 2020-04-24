# 203. Remove Linked List Elements

# Remove all elements from a linked list of integers that have value val.

# Example:
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        while head != None and head.val == val:
            head = head.next
        current = head
        while current != None:
            if current.next != None and current.next.val == val:
                current = current.next.next
            else:
                current = current.next
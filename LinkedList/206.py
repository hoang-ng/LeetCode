# 206. Reverse Linked List

# Reverse a singly linked list.

# Example:
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL

# Follow up:
# A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        prev = None
        current = head
        while current != None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
    
    def reverseList2(self, head):
        if head == None:
            return None
        if head.next == None:
            return head
        node = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return node
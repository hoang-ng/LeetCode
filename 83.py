# 83. Remove Duplicates from Sorted List

# Given a sorted linked list, delete all duplicates such that each element appear only once.

# Example 1:
# Input: 1->1->2
# Output: 1->2

# Example 2:
# Input: 1->1->2->3->3
# Output: 1->2->3

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        current = head
        while current != None and current.next != None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
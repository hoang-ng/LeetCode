# 61. Rotate List

# Given a linked list, rotate the list to the right by k places, where k is non-negative.

# Example 1:
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL

# Example 2:
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        if head == None or head.next == None:
            return head
        
        current = head
        count = 0
        lastNode = None
        while current != None:
            if current.next == None:
                lastNode = current
            current = current.next
            count += 1
        k = k % count
        
        i = 0
        first = head
        second = head
        while i <= k:
            first = first.next
            i += 1
        while first != None:
            first = first.next
            second = second.next
        
        lastNode.next = head
        head = second.next
        second.next = None
        
        return head
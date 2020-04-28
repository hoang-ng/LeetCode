# 92. Reverse Linked List II

# Reverse a linked list from position m to n. Do it in one-pass.
# Note: 1 ≤ m ≤ n ≤ length of list.

# Example:
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        prev = None
        current = head
        index = 0
        
        while current != None and index < m - 1:
            prev = current
            current = current.next
            index += 1
        
        startNode = prev
        endNode = current
            
        while current != None and index < n:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            index += 1
            
        if startNode != None:
            startNode.next = prev
        endNode.next = current
        return prev

listNode = ListNode(1)
listNode.next = ListNode(2)
listNode.next.next = ListNode(3)
listNode.next.next.next = ListNode(4)
listNode.next.next.next.next = ListNode(5)

sol = Solution()
sol.reverseBetween(listNode, 1, 5)
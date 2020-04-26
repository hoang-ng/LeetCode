# 234. Palindrome Linked List

# Given a singly linked list, determine if it is a palindrome.

# Example 1:
# Input: 1->2
# Output: false

# Example 2:
# Input: 1->2->2->1
# Output: true

# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        slow = self.reverseLinkedList(slow)
        fast = head
        
        while slow != None and fast != None and slow.val == fast.val:
            slow = slow.next
            fast = fast.next
        
        if slow == None:
            return True
        return False
        
    def reverseLinkedList(self, head):
        prev = None
        current = head
        while current != None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
# 2. Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        
        current1 = l1
        current2 = l2
        
        carry = 0
        while current1 != None or current2 != None or carry != 0:
            val1 = 0 if current1 == None else current1.val
            val2 = 0 if current2 == None else current2.val
            
            val = val1 + val2 + carry
            newNode = ListNode(val % 10)
            current.next = newNode
            current = newNode
            carry = val // 10
            
            if current1 != None:
                current1 = current1.next
            if current2 != None:
                current2 = current2.next
                   
        return dummy.next
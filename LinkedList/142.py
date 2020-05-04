# 142. Linked List Cycle II

# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
# Note: Do not modify the linked list.

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.

# Example 2:
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.

# Example 3:
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.

# Follow-up:
# Can you solve it without using extra space?

from ListNode import *

class Solution(object):
    def detectCycle(self, head):
        arr = set()
        current = head
        while current != None:
            if current in arr:
                return current
            else:
                arr.add(current)
            current = current.next
        
        return None
    
    def detectCycle2(self, head):
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                while head != slow:
                    head = head.next
                    slow = slow.next
                return slow
        
        return None

node = ListNode(1)
node.next = ListNode(2)
node3 = node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)
node.next.next.next.next.next = node3

sol = Solution()
sol.detectCycle2(node)
# 24. Swap Nodes in Pairs

# Given a linked list, swap every two adjacent nodes and return its head.
# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Example:
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        current = head
        prevNode = dummy
        nextNode = current.next
        
        while prevNode!= None and current != None and nextNode != None:
            temp1 = nextNode.next
            nextNode.next = current
            prevNode.next = nextNode
            prevNode = current
            current = temp1
            if current != None:
                nextNode = current.next
            
        if nextNode == None:
            prevNode.next = current
        if current == None:
            prevNode.next = None
        return dummy.next
    
    def swapPairs2(self, head):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        while current and current.next and current.next.next:
            first = current.next
            second = current.next.next
            third = second.next
            current.next = second
            second.next = first
            first.next = third
            current = first
        
        return dummy.next

node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)
node.next.next.next.next.next = ListNode(6)

sol = Solution()
sol.swapPairs(node)
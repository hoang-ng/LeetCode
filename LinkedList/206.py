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
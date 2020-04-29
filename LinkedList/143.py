# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        arr = []
        self.reverseList(head, arr)
        
        current = head
        for i in range(0, len(arr)):
            if current == arr[i]:
                current.next = None 
                break
            if arr[i] == current.next:
                arr[i].next = None
                break
            arr[i].next = current.next
            current.next = arr[i]
            current = arr[i].next
        return head
        
    def reverseList(self, head, arr):
        if head != None:
            self.reverseList(head.next, arr)
            arr.append(head)
    
    def reorderList2(self, head):
        if not head:
            return
        
        mid = find_middle(head)
        tail = reverse(mid.next)
        mid.next = None
        
        merge(head, tail)


def find_middle(head):
    slow = fast = head
    
    while fast and fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    
    return slow
        

def reverse(head):
    prev = None
    
    cur = head
    while cur:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp
    
    return prev


def merge(l1, l2):
    dummy_head = ListNode(0)
    cur = dummy_head
    
    while l1 or l2:
        cur.next = l1
        cur = cur.next
        l1 = l1.next
        l1, l2 = l2, l1
    
    return dummy_head.next

node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)
node.next.next.next.next.next = ListNode(6)

sol = Solution()
sol.reorderList(node)
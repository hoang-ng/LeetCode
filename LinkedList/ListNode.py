
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createLinkedList(array):
    dummy = ListNode(0)
    current = dummy
    for i in range(len(array)):
        current.next = ListNode(array[i])
        current = current.next
    return dummy.next
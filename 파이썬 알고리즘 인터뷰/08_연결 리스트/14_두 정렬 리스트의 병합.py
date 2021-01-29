# 정렬되어 있는 두 연결 리스트를 합쳐라.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(5)
next_node = Node(12)
head.next = next_node

def mergeTwoLists(l1, l2):
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = self.mergeTwoLists(l1.next, l2)
    return l1
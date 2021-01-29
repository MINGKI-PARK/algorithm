# 연결 리스트가 팰린드롬 구조인지 판별하라.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node = ListNode(1, 5)
print(node.val)
print(node.val)
print(node.next)
node = node.next
print(node.val)


def isPalindrome(head):
    q: list = []

    if not head:
        return True

    node = head
    # 리스트 변환
    while node is not None:
        q.append(node.val)
        node = node.next

    # 펠린드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False
    
    return True

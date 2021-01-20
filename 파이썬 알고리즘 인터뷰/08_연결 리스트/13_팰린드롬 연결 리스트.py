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
    pass
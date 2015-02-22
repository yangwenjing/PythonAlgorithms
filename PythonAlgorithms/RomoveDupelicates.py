__author__ = 'yangwenjing'



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    head = None

    def __init__(self):
        self.head = ListNode(1)
        self.head.next = ListNode(1)

    def deleteDuplicates(self, head):

        if head is None:
            return None

        node = head
        node_next = head.next
        while not node_next is None:
            if node_next.val == node.val:
                node_next = node_next.next
                node.next = node_next
            else:
                node = node_next
                node_next = node.next

        return head

s = Solution()
node = s.deleteDuplicates(s.head)

while node is not None:
    print node.val
    node = node.next

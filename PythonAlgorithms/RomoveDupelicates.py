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
        self.head.next = ListNode(2)
        self.head.next.next = ListNode(2)

    def deleteDuplicates2(self, head):

        if head is None:
            return None
        node = head
        node_next = node.next
        head2 = next_node = None

        while node is not None:

            if node_next is not None and node.val == node_next.val:
                val = node.val
                while node_next is not None and node_next.val == val:
                    node_next = node_next.next

                node = node_next
                node_next = node_next.next if node_next else None

            else:

                if head2 is None:
                    head2 = node
                    head2.next = None
                    next_node = head2
                else:
                    next_node.next = node
                    next_node = node
                    next_node.next = None

                node = node_next
                node_next = node_next.next if node_next else None

        return head2

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
node = s.deleteDuplicates2(s.head)

while node is not None:
    print node.val
    node = node.next

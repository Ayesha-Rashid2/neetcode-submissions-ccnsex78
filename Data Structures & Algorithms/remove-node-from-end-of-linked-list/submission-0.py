class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        nodes = []

        while cur:
            nodes.append(cur)
            cur = cur.next

        traverse = len(nodes) - n

        if traverse == 0:
            return head.next

        nodes[traverse - 1].next = nodes[traverse].next
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        #Find the middle value
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        prev = slow.next = None


        # Reverses the second half of the linked list --> now go, <--
        while second_half:
            temp = second_half.next
            second_half.next = prev
            prev = second_half 
            second_half = temp

        # merge the two halves
        first = head
        second = prev

        while first and second:
            temp1, temp2 = first.next, second.next

            first.next = second
            second.next = temp1
            first, second = temp1, temp2



        




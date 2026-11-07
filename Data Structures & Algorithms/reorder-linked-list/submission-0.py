# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def find_mid(head):
            slow = head 
            fast = head.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next 
            return slow

        def reverse(head):
            curr = head
            prev = None

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return prev


        def merge(l1, l2):
            while l2:
                tmp1 = l1.next
                tmp2 = l2.next

                l1.next = l2
                l2.next = tmp1

                l1 = tmp1
                l2 = tmp2

        mid = find_mid(head)
        l2 = reverse(mid.next)
        mid.next = None

        merge(head, l2)

    
        


            
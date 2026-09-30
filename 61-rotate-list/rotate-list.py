# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if head is None:
            return None
        n=1
        last = head
        while(last.next is not None ):
            n+=1
            last = last.next
        k = k%n
        if k ==0:
            return head
        count = 1
        t = head
        while (t is not None):
            if (count ==n-k):
                break
            count+=1
            t = t.next
        last.next = head
        res = t.next
        t.next = None
        return res
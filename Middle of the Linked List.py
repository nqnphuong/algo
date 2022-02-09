# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # tao ra 2 con tro truoc va sau: con tro sau nhanh hon con tro truoc 2 buoc
        pre = post = head
        while post and post.next:
            pre = pre.next
            post = post.next.next
        return pre

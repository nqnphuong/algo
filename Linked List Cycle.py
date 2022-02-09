# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        res = head
        st = set()  # tao set de kiem tra node co xuat hien lai nua khong
        while res:
            if res in st:
                return True
            st.add(res)
            res = res.next
        return False




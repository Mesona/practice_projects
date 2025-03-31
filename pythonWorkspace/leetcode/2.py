# https://leetcode.com/problems/add-two-numbers/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ten = 0
        while l1 is not None or l2 is not None or ten == 1:
            if l1 is None and l2 is None and ten == 1:
                val = 1
            elif l1 is None:
                val = l2.val + ten
            elif l2 is None:
                val = l1.val + ten
            else:
                val = l1.val + l2.val + ten
                
            if val > 9:
                val = val - 10
                ten = 1
            else:
                ten = 0
            
            try:
                l1 = l1.next
            except:
                pass
                
            try:
                l2 = l2.next
            except:
                pass
                
            if 'l3' in locals():
                current_l3.next = ListNode(val)
                current_l3 = current_l3.next
            else:
                l3 = ListNode(val)
                current_l3 = l3
                
        return l3
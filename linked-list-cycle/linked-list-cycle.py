# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        li =[]
        u=head
        while (u):
            if u in li:
                return True
            else:
                li.append(u)
                u= u.next
        return False    
        
        
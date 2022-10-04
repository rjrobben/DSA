# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA = headA
        hashMap = {}
        while currA:
            hashMap[currA] = 1
            currA = currA.next
            
        currB = headB
        while currB:
            if currB in hashMap:
                return currB
            currB = currB.next
            
        return None

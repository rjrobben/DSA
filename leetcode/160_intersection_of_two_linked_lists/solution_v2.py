# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA and headB:
            A, B = headA, headB
            while A!=B:
                A = A.next if A else headB
                B = B.next if B else headA
            return A

# let headA length = m, headB length = n, Intersection = I

# Case 1: Have intersection

# for pointer A, he walks A---...---I---...---None-B-...--I---...---None |
# for pointer B, he walks B-...--I---...---None-A---...---I---...---None | 

# if m==n, how they will meet is straightforward. 

# if m!=n: 
# for pointer A, it requires n + (m-I) steps to reach the second I.
# for pointer B, it require m + (n-I) steps to reach the second I. 

# hence, two pointers will meet at second Intersection where A == B to end the while loop and exit
# Otherwise, as m!=n, they start at different position, the longer one must be faster than the shorter one even if the shorter one pointer goes to longer one faster. 

# Case 2: no intersection

# for pointer A, he walks A---...---None-B-...--None|
# for pointer B, he walks B-...--None-A---...---None|

# A will be equal to B when bothe pointer achieve None the same time, otherwise both chain is on different memory location and won't meet

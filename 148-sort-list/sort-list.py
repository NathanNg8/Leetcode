# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = []
        current = head
        while current:
            temp.append(current.val) 
            current = current.next
        temp.sort()
        dummy = ListNode(0)
        current = dummy
        for num in temp:
            current.next = ListNode(num)
            current = current.next
        return dummy.next
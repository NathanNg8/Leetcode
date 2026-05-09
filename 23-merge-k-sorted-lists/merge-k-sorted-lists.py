# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        store = []

        for linked_list in lists:
            curr = linked_list

            while curr:
                store.append(curr.val)
                curr = curr.next

        store.sort()

        dummy = ListNode(0)
        curr = dummy

        for value in store:
            curr.next = ListNode(value)
            curr = curr.next

        return dummy.next 


        
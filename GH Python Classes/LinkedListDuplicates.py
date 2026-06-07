
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """


        # Start at the beginning of the list
        current = head

        # Traverse until we hit the end of the list
        while current and current.next:
            # If the current node's value is the same as the next node's
            if current.val == current.next.val:
                # "Skip" the next node by linking to the one after it
                current.next = current.next.next
            else:
                # Otherwise, just move the pointer forward
                current = current.next

        print(head)

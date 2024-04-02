# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to start the merged list
        dummy = ListNode()
        # Pointer to traverse the merged list
        ptr = dummy

        # Traverse both lists simultaneously until one of them reaches the end
        while list1 and list2:
            if list1.val < list2.val:
                # If the value in list1 is smaller, append it to the merged list
                ptr.next = list1
                list1 = list1.next
            else:
                # If the value in list2 is smaller or equal, append it to the merged list
                ptr.next = list2
                list2 = list2.next
            # Move the pointer to the next node in the merged list
            ptr = ptr.next
    
        # If any list still has remaining nodes, append them to the merged list
        if list1:
            ptr.next = list1
        elif list2:
            ptr.next = list2

        # Return the next of the dummy node, which is the head of the merged list
        return dummy.next

# Time Complexity:
# The time complexity of this solution is O(m + n), where m and n are the lengths of the two input linked lists. This is because the algorithm traverses both lists simultaneously, comparing and appending nodes until one of the lists reaches the end.

# Space Complexity:
# The space complexity is O(1) because the extra space used does not depend on the size of the input. The algorithm only uses a constant amount of extra space for pointers and the dummy node.

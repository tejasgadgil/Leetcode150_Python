class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle the case where the target node is the head
        dummy = ListNode(0, head)
        # Initialize two pointers: dist and head
        dist = dummy

        # Move the head pointer forward by n steps
        while n > 0 and head:
            head = head.next
            n -= 1
        
        # Move both pointers until the head pointer reaches the end of the list
        while head is not None:
            head = head.next
            dist = dist.next

        # Remove the nth node from the end by adjusting the next pointer of the preceding node
        dist.next = dist.next.next
        
        # Return the head of the modified list (excluding the dummy node)
        return dummy.next

# This solution effectively removes the nth node from the end of the linked list using the two-pointer technique, 
# with one pointer (head) moving ahead by n steps before the second pointer (dist) starts moving. 
# The time complexity is O(L), where L is the length of the linked list, as we traverse the list only once. 
# The space complexity is O(1) since we use constant extra space.

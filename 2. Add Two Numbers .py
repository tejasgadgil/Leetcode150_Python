class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize variables for the starting node of the result and carry
        start = result = ListNode()
        carry = 0

        # Iterate through both linked lists until either one reaches the end
        while l1 is not None or l2 is not None: 
            # Extract the values of the current nodes, handling the case where one of the lists has reached the end
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum of the current digits and the carry
            sum = val1 + val2 + carry
            carry = sum // 10

            # Create a new node with the sum modulo 10 and link it to the result list
            result.next = ListNode(sum % 10)
            result = result.next

            # Move to the next nodes in both lists, handling the case where one of the lists has reached the end
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # If there's a remaining carry, create a new node for it
        if carry > 0:
            result.next = ListNode(carry)

        # Return the next node after the starting node, which is the head of the result list
        return start.next

# The time complexity is O(max(m, n)), where m and n are the lengths of the input linked lists. 
# The space complexity is O(max(m, n)) for the resulting linked list.

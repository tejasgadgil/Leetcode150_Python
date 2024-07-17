# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import List, Optional

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []  # Initialize the result list which will store levels of the tree
        if root == None: 
            return result  # If root is None, return an empty list
        
        queue = deque([root])  # Use a deque to facilitate O(1) popleft operations
        
        while len(queue) != 0:  # Continue until the queue is empty
            size = len(queue)  # Number of nodes at the current level
            sublist = []  # List to store the values of nodes at the current level
            
            for i in range(size):
                node = queue.popleft()  # Pop the leftmost node in the queue
                if node.left != None: 
                    queue.append(node.left)  # Add the left child to the queue if it exists
                if node.right != None: 
                    queue.append(node.right)  # Add the right child to the queue if it exists
                
                sublist.append(node.val)  # Add the value of the current node to the sublist
            
            result.append(sublist)  # Add the sublist of the current level to the result
        
        return result  # Return the list of levels

'''
Approach:
While the queue is not empty, repeat the following steps:
 - Get the number of nodes at the current level (`size`).
 - Initialize an empty sublist to store the values of the nodes at the current level.
 - For each node at the current level:
       - Dequeue a node from the front of the queue.
       - If the node has a left child, enqueue it.
       - If the node has a right child, enqueue it.
       - Add the value of the node to the sublist.
  - Append the sublist to the result list.

Time Complexity: O(n)
- Each node is processed exactly once, where n is the number of nodes in the tree.

Space Complexity: O(n)
- The space complexity is O(n) due to the additional space used by the queue to store nodes and the result list to store the output.
'''

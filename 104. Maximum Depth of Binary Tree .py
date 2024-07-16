# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: if the root is None, the depth is 0
        if root is None:
            return 0
        
        # Recursively find the depth of the left subtree
        leftHeight = self.maxDepth(root.left)
        # Recursively find the depth of the right subtree
        rightHeight = self.maxDepth(root.right)
        
        # The depth of the current node is 1 + the maximum of the depths of the subtrees
        return 1 + max(leftHeight, rightHeight)

# Time Complexity: O(n)
# Space Complexity: O(h)

# Approach:
# 1. Use recursion to find the maximum depth of the left and right subtrees.
# 2. The maximum depth of the tree is 1 + the maximum depth of the left and right subtrees.
# 3. If the root is None, return 0 as the base case.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from TreeNode import TreeNode
from typing import Optional

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxdiameter: int = 0
        
        def diameterOfBinaryTreeRecursive(root: Optional[TreeNode]) -> int:

            nonlocal maxdiameter

            if not root:
                return 0
            
            leftheight: int = 0
            rightheight: int = 0

            if root.left:
                leftheight =  diameterOfBinaryTreeRecursive(root.left)
            
            if root.right:
                rightheight = diameterOfBinaryTreeRecursive(root.right)
            
            maxdiameter = max(maxdiameter, leftheight + rightheight)

            maxpath = max(rightheight, leftheight)
            return maxpath+1

        diameterOfBinaryTreeRecursive(root)
        return maxdiameter
    
if __name__ == "__main__":
    # Test case 1: Example tree [1, 2, 3, 4, 5]
    #      1
    #     / \
    #    2   3
    #   / \
    #  4   5
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node2 = TreeNode(2, node4, node5)
    node3 = TreeNode(3)
    root = TreeNode(1, node2, node3)
    solution = Solution()
    diameter = solution.diameterOfBinaryTree(root)
    print("Diameter of binary tree (Test 1):", diameter, "Expected: 3")

    # Test case 2: Only root node
    root2 = TreeNode(1)
    diameter2 = solution.diameterOfBinaryTree(root2)
    print("Diameter of binary tree (Test 2):", diameter2, "Expected: 0")

    # Test case 3: Linear tree (left-skewed)
    # 1 -> 2 -> 3 -> 4
    root3 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    diameter3 = solution.diameterOfBinaryTree(root3)
    print("Diameter of binary tree (Test 3):", diameter3, "Expected: 3")

    # Test case 4: Linear tree (right-skewed)
    # 1 -> 2 -> 3 -> 4
    root4 = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    diameter4 = solution.diameterOfBinaryTree(root4)
    print("Diameter of binary tree (Test 4):", diameter4, "Expected: 3")

    # Test case 5: Empty tree
    diameter5 = solution.diameterOfBinaryTree(None)
    print("Diameter of binary tree (Test 5):", diameter5, "Expected: 0")
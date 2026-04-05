from TreeNode import TreeNode
from typing import Optional, List
from collections import deque

class LevelOrderTraversal:
     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result: List[List[int]] = []

        if not root:
            return result

        queue: deque = deque([root])
        
        while queue:
            levelNodes: int = len(queue)
            levelNodesList: List[int] = []

            for _ in range(levelNodes):
                current: TreeNode = queue.popleft()

                if current.left:
                    queue.append(current.left)
                
                if current.right:
                    queue.append(current.right)
                
                levelNodesList.append(current.val)
            result.append(levelNodesList)
        
        return result
     
# Place test code after class definition
if __name__ == "__main__":
    # Test 1: Balanced tree
    #      1
    #     / \
    #    2   3
    #   / \   \
    #  4   5   6
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node2 = TreeNode(2, node4, node5)
    node3 = TreeNode(3, None, node6)
    root = TreeNode(1, node2, node3)
    traversal = LevelOrderTraversal()
    result1 = traversal.levelOrder(root)
    print("Test 1 result:", result1, "Expected: [[1], [2, 3], [4, 5, 6]]")

    # Test 2: Single node
    root2 = TreeNode(10)
    result2 = traversal.levelOrder(root2)
    print("Test 2 result:", result2, "Expected: [[10]]")

    # Test 3: Left-skewed tree
    # 1 -> 2 -> 3
    root3 = TreeNode(1, TreeNode(2, TreeNode(3)))
    result3 = traversal.levelOrder(root3)
    print("Test 3 result:", result3, "Expected: [[1], [2], [3]]")

    # Test 4: Empty tree
    result4 = traversal.levelOrder(None)
    print("Test 4 result:", result4, "Expected: []")
     
    
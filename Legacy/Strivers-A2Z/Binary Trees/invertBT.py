from typing import List, Optional
from buildBT import TreeNode, build_tree


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        # Swap the left and right children
        root.left, root.right = root.right, root.left

        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# Test case 1
tree_list = [4, 2, 7, 1, 3, 6, 9]
root = build_tree(tree_list)
obj = Solution()
print(obj.invertTree(root))

# Test case 2
tree_list = [2, 1, 3]
root = build_tree(tree_list)
obj = Solution()
print(obj.invertTree(root))

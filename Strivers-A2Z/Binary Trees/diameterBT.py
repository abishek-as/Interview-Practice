from typing import Optional
from buildBT import TreeNode, build_tree


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0  # height = 0 for null nodes

            # Recursively find the height of left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # Diameter at this node = left height + right height
            self.max_diameter = max(
                self.max_diameter, left_height + right_height)

            # Height to return = 1 + max of left and right heights
            return 1 + max(left_height, right_height)

        dfs(root)
        return self.max_diameter


# Test case 1
tree_list = [1, 2, 3, 4, 5]
root = build_tree(tree_list)
obj = Solution()
print(obj.diameterOfBinaryTree(root))

# Test case 2
tree_list = [1, 2]
root = build_tree(tree_list)
obj = Solution()
print(obj.diameterOfBinaryTree(root))

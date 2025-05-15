from typing import Optional, List
from buildBT import TreeNode, build_tree


class Solution:
    def boundaryTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # Result list to store the boundary nodes
        boundary = []

        # Helper function to check if a node is a leaf
        def is_leaf(node: TreeNode) -> bool:
            return node.left is None and node.right is None

        # Add all left boundary nodes (excluding leaves)
        def add_left_boundary(node: Optional[TreeNode]):
            while node:
                if not is_leaf(node):
                    boundary.append(node.val)
                # Move to the next left boundary node
                if node.left:
                    node = node.left
                else:
                    node = node.right

        # Add all leaf nodes (left to right)
        def add_leaf_nodes(node: Optional[TreeNode]):
            if node:
                if is_leaf(node):
                    boundary.append(node.val)
                add_leaf_nodes(node.left)
                add_leaf_nodes(node.right)

        # Add all right boundary nodes (excluding leaves, collected in reverse)
        def add_right_boundary(node: Optional[TreeNode]):
            temp = []
            while node:
                if not is_leaf(node):
                    temp.append(node.val)
                # Move to the next right boundary node
                if node.right:
                    node = node.right
                else:
                    node = node.left
            # Add right boundary nodes in reverse order
            while temp:
                boundary.append(temp.pop())

        # Step 1: Add root (if not a leaf)
        if not is_leaf(root):
            boundary.append(root.val)

        # Step 2: Add left boundary
        add_left_boundary(root.left)

        # Step 3: Add all leaf nodes
        add_leaf_nodes(root)

        # Step 4: Add right boundary
        add_right_boundary(root.right)

        return boundary


# Example 1
tree_nodes = [1, 2, 7, 3, None, None, 8, None, 4, 9, None, 5, 6, 10, 11]
root = build_tree(tree_nodes)
sol = Solution()
print("Boundary Traversal:", sol.boundaryTraversal(root))
# Output: [1, 2, 3, 4, 5, 6, 10, 11, 9, 8, 7]

# Example 2
tree_nodes = [10, 5, 20, 3, 8, 18, 25, None, 7, None, None]
root = build_tree(tree_nodes)
sol = Solution()
print("Boundary Traversal:", sol.boundaryTraversal(root))
# Output: [10, 5, 3, 7, 8, 18, 25, 20]

# Example 3
tree_nodes = [1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, None, None]
root = build_tree(tree_nodes)
sol = Solution()
print("Boundary Traversal:", sol.boundaryTraversal(root))
# Output: [10, 5, 3, 7, 8, 18, 25, 20]

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


def build_tree(nodes):
    if not nodes or nodes[0] is None:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        current = queue.pop(0)
        if i < len(nodes) and nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1
    return root


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

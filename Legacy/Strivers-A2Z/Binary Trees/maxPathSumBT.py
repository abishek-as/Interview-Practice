from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize result with the smallest possible value
        self.max_sum = float('-inf')

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            # Get max path sum from left and right children
            # If negative, we discard it by taking max with 0
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)

            # Path sum including both children and the node (split case)
            current_path_sum = node.val + left_max + right_max

            # Update global max path sum if current path is better
            self.max_sum = max(self.max_sum, current_path_sum)

            # Return max sum path *including* the current node and one subtree
            return node.val + max(left_max, right_max)

        dfs(root)
        return self.max_sum


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
tree_list = [1, 2, 3]
root = build_tree(tree_list)
obj = Solution()
print(obj.maxPathSum(root))

# Test case 2
tree_list = [-10, 9, 20, None, None, 15, 7]
root = build_tree(tree_list)
obj = Solution()
print(obj.maxPathSum(root))

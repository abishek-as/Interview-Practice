from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node: Optional[TreeNode]) -> Tuple[bool, int]:
            if not node:
                return True, 0  # (is_balanced, height)

            left_balanced, left_height = check(node.left)
            right_balanced, right_height = check(node.right)

            is_balanced = (
                left_balanced and
                right_balanced and
                abs(left_height - right_height) <= 1
            )
            height = 1 + max(left_height, right_height)

            return is_balanced, height

        return check(root)[0]


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
tree_list = [3, 9, 20, None, None, 15, 7]
root = build_tree(tree_list)
obj = Solution()
print(obj.isBalanced(root))

# Test case 2
tree_list = [1, 2, 2, 3, 3, None, None, 4, 4]
root = build_tree(tree_list)
obj = Solution()
print(obj.isBalanced(root))

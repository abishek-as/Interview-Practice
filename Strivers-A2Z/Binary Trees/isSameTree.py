from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are None, trees match at this point
        if p is None and q is None:
            return True
        # If one of them is None or values don't match, trees differ
        if p is None or q is None or p.val != q.val:
            return False

        # Recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


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
p, q = [1, 2, 3], [1, 2, 3]
root_p = build_tree(p)
root_q = build_tree(q)
obj = Solution()
print(obj.isSameTree(root_p, root_q))

# Test case 2
p, q = [1, 2], [1, None, 2]
root_p = build_tree(p)
root_q = build_tree(q)
obj = Solution()
print(obj.isSameTree(root_p, root_q))

# Test case 3
p, q = [1, 2, 1], [1, 1, 2]
root_p = build_tree(p)
root_q = build_tree(q)
obj = Solution()
print(obj.isSameTree(root_p, root_q))

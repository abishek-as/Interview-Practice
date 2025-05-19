from typing import Optional
from buildBT import TreeNode, build_tree


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


# # Test case 1
# p, q = [1, 2, 3], [1, 2, 3]
# root_p = build_tree(p)
# root_q = build_tree(q)
# obj = Solution()
# print(obj.isSameTree(root_p, root_q))

# # Test case 2
# p, q = [1, 2], [1, None, 2]
# root_p = build_tree(p)
# root_q = build_tree(q)
# obj = Solution()
# print(obj.isSameTree(root_p, root_q))

# Test case 3
p, q = [1, 2, 1], [1, 1, 2]
root_p = build_tree(p)
root_q = build_tree(q)
obj = Solution()
print(obj.isSameTree(root_p, root_q))

from typing import Optional
from buildBT import TreeNode, build_tree


class Solution:
    def isSubtree(self, main_root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        # If the subtree is empty, it's always a subtree of any tree (including an empty one)
        if sub_root is None:
            return True

        # If the main tree is empty but subtree is not, then it can't contain the subtree
        if main_root is None:
            return False

        # If the trees match from the current node, return True
        if self.sameTree(main_root, sub_root):
            return True

        # Otherwise, recursively check left and right subtrees of the main tree
        return (self.isSubtree(main_root.left, sub_root) or
                self.isSubtree(main_root.right, sub_root))

    def sameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Both nodes are None: trees are equal up to this branch
        if root1 is None and root2 is None:
            return True

        # Both nodes are not None and values are equal: check subtrees
        if root1 and root2 and root1.val == root2.val:
            return (self.sameTree(root1.left, root2.left) and
                    self.sameTree(root1.right, root2.right))

        # Trees do not match
        return False


# Test case 1
root_list = [3, 4, 5, 1, 2]
sub_root_list = [4, 1, 2]
root_tree = build_tree(root_list)
sub_tree = build_tree(sub_root_list)
solution = Solution()
print(solution.isSubtree(root_tree, sub_tree))  # Expected: True

# Test case 2
root_list = [3, 4, 5, 1, 2, None, None, None, None, 0]
sub_root_list = [4, 1, 2]
root_tree = build_tree(root_list)
sub_tree = build_tree(sub_root_list)
solution = Solution()
print(solution.isSubtree(root_tree, sub_tree))  # Expected: False

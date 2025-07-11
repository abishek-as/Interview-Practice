from collections import deque
from typing import Optional
from buildBT import TreeNode, build_tree
# Your solution


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1

    def bfs(self, root: TreeNode) -> int:
        if root is None:
            return 0

        level = 0
        q = deque([root])

        while q:
            for i in range(len(q)):
                current = q.popleft()
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            level += 1
        return level

    def IterativeBfs(self, root: TreeNode) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res


# Example usage
tree_list = [3, 9, 20, None, None, 15, 7]
root = build_tree(tree_list)
sol = Solution()
print(sol.maxDepth(root))  # Output should be 3
print(sol.bfs(root))  # Output should be 3
print(sol.IterativeBfs(root))  # Output should be 3

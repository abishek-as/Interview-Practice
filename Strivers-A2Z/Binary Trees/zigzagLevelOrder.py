from typing import List, Optional
from buildBT import TreeNode, build_tree


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Result list to store the final zigzag traversal
        res = []

        # Queue to help with level order traversal, implemented using a list
        q = [root] if root else []

        # Traverse through the tree level by level
        while q:
            level = []
            # Process all nodes at the current level
            for _ in range(len(q)):
                node = q.pop(0)  # Pop the first element (simulate dequeue)
                level.append(node.val)

                # Add left and right children to the queue for next level processing
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # Reverse the level order for every odd level (zigzag effect)
            if len(res) % 2 != 0:
                level = level[::-1]  # Reverse the level for zigzag pattern
            res.append(level)

        return res


# Test case 1
tree_list = [3, 9, 20, None, None, 15, 7]
root = build_tree(tree_list)
obj = Solution()
print(obj.zigzagLevelOrder(root))

# Test case 2
tree_list = [1]
root = build_tree(tree_list)
obj = Solution()
print(obj.zigzagLevelOrder(root))

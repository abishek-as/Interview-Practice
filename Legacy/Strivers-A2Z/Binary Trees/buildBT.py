from typing import Optional, List


class TreeNode:
    """
    Definition for a binary tree node.
    """

    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Builds a binary tree from a list of values in level-order (BFS) format.
    None indicates absence of a node.

    Example:
        Input : [1, 2, 3, None, 4]
        Tree  :    1
                 / \
                2   3
                 \
                  4

    Args:
        nodes (List[Optional[int]]): List representing level-order traversal.

    Returns:
        TreeNode: Root of the constructed binary tree.
    """

    # Edge case: empty list or root is None
    if not nodes or nodes[0] is None:
        return None

    # Create the root node
    root = TreeNode(nodes[0])

    # Queue to keep track of nodes whose children need to be assigned
    queue = [root]

    # Index in the list starting from the second element
    i = 1

    # Loop through the list and build the tree
    while queue and i < len(nodes):
        current = queue.pop(0)

        # Assign left child if available
        if i < len(nodes) and nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1

        # Assign right child if available
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1

    return root

# BT Node definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Function to build a binary tree from a list of values
def build_tree(nodes):

    # Check if the list is empty or the first element is None
    if not nodes or nodes[0] is None:
        return None

    # Create the root node
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1

    while queue and i < len(nodes):
        current = queue.pop(0)

        # Assign left child
        if i < len(nodes) and nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1

        # Assign right child
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1
    return root


tree_list = [3, 9, 20, None, None, 15, 7]
root = build_tree(tree_list)
print(root.val)

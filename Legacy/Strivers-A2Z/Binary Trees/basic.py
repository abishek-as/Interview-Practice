from collections import deque


# Node class for Binary Tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Binary Tree class
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_level_order(self, values):
        """Inserts values into the tree in level-order to form a complete binary tree."""
        if not values:
            return None

        self.root = Node(values[0])
        queue = deque([self.root])
        i = 1

        while i < len(values):
            current = queue.popleft()
            if i < len(values):
                current.left = Node(values[i])
                queue.append(current.left)
                i += 1
            if i < len(values):
                current.right = Node(values[i])
                queue.append(current.right)
                i += 1

    # DFS Traversals
    def dfs_preOrder(self, node):
        if not node:
            return []
        return (
            [node.value] +
            self.dfs_preOrder(node.left) + self.dfs_preOrder(node.right)
        )

    def dfs_inOrder(self, node):
        if not node:
            return []
        return self.dfs_inOrder(node.left) + [node.value] + self.dfs_inOrder(node.right)

    def dfs_postOrder(self, node):
        if not node:
            return []
        return (
            self.dfs_postOrder(node.left)
            + self.dfs_postOrder(node.right)
            + [node.value]
        )

    # BFS Traversal
    def bfs(self):
        if not self.root:
            return []

        queue = deque([self.root])
        result = []

        while queue:
            current = queue.popleft()
            result.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return result


# Instantiate and build the tree
bt = BinaryTree()
bt.insert_level_order(list(range(15)))  # 0 to 14

# Perform Traversals
print("DFS Preorder:", bt.dfs_preOrder(bt.root))
print("DFS Inorder:", bt.dfs_inOrder(bt.root))
print("DFS Postorder:", bt.dfs_postOrder(bt.root))
print("BFS:", bt.bfs())

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
    def dfs_preorder(self, node):
        if not node:
            return []
        return (
            [node.value] + self.dfs_preorder(node.left) + self.dfs_preorder(node.right)
        )

    def dfs_inorder(self, node):
        if not node:
            return []
        return self.dfs_inorder(node.left) + [node.value] + self.dfs_inorder(node.right)

    def dfs_postorder(self, node):
        if not node:
            return []
        return (
            self.dfs_postorder(node.left)
            + self.dfs_postorder(node.right)
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
print("DFS Preorder:", bt.dfs_preorder(bt.root))
print("DFS Inorder:", bt.dfs_inorder(bt.root))
print("DFS Postorder:", bt.dfs_postorder(bt.root))
print("BFS:", bt.bfs())

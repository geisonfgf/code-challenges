"""
Insert in a BinarySearchTree(BST)

Expected result:
      1
    /  \
   2   3
 /  \ / \
4   5 6 7
"""

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, root, value):
        if root is None:
            return
        
        stack = deque()
        stack.append(root)
        node = root

        while stack:
            node = stack.pop()
            if value < node.data and node.left:
                stack.append(node.left)
            elif node.right:
                stack.append(node.right)
            if node.left is None and node.right is None:
                node.left = Node(value)
            elif node.left and node.right is None:
                node.right = Node(value)

    def get_height(self, node):
        if node is None:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))

    
    def __str_tree_builder(self, node, level):
        str_tree = []
        if node:
            str_tree.append(self.__str_tree_builder(node.right, level + 1))
            str_tree.append("| " * level)
            str_tree.append(
                ''.join([str(node.data), "\n"]))
            str_tree.append(self.__str_tree_builder(node.left, level + 1))
        return ''.join(str_tree)

    def __repr__(self):
        return self.__str_tree_builder(self, 0)

root = Node(1)
root.insert(root, 2)
root.insert(root, 3)
root.insert(root, 4)
root.insert(root, 5)
root.insert(root, 6)
root.insert(root, 7)

print "BST height is:", root.get_height(root)
print root
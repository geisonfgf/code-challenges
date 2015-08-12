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
            if node.left is None and node.right is None:
                node.left = Node(value)
                break
            elif node.left and node.right is None:
                node.right = Node(value)
                break
            print str(value) + " - " + str(node.data)
            if value < node.data:
                if node.left:
                    stack.append(node.left)
            else:
                if node.right:
                    stack.append(node.right)
            
    
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

print root
"""
Print Top View of BinaryTree

      1
    /   \
   2    3
  / \    \
4   5    6
     \   \
     7    8

Expected result: 4 2 1 3 6 8
"""

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def top_view(root):
    if root is None:
        return

    nodes_to_print = []
    levels = []
    queue = deque()
    queue.append([root, 0])

    while queue:
        node, level = queue.popleft()
        if level not in levels:
            levels.append(level)
            nodes_to_print.append([level, str(node.data)])

        if node.left:
            queue.append([node.left, level - 1])
        if node.right:
            queue.append([node.right, level + 1])

    for index, value in enumerate(sorted(nodes_to_print)):
        print value[1],


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.right = Node(6)
root.right.right.right = Node(8)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(7)

top_view(root)
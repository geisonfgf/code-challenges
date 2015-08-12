"""
Print in Level Order

          1
       /    \
      2     3
    /  \  /  \
   4   5  6  7
  /
 8 

Expected result: 1 2 3 4 5 6 7 8
"""

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_in_level_order(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while queue:
        node_count = len(queue)
        while node_count > 0:
            node = queue.popleft()
            print str(node.data),
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            node_count -= 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)

print_in_level_order(root)
from collections import deque

class Node:
    def __init__(self, data, level=0):
        self.data = data
        self.left = None
        self.right = None

def in_order(node):
    if node is None: return
    in_order(node.left)
    print str(node.data) + " ",
    in_order(node.right)

def swap_subtree_of_level(node, k):
    if node is None: return

    queue = deque()
    queue.append(node)
    queue.append(None)
    level = 1

    while queue:
        tmp = queue.popleft()
        if tmp is None:
            if queue:
                queue.append(None)
            level += 1
        else:
            if level == k:
                swap = tmp.left
                tmp.left = tmp.right
                tmp.right = swap
            if tmp.left:
                queue.append(tmp.left)
            if tmp.right:
                queue.append(tmp.right)


# Building the tree
tree_number_of_nodes = int(input())
root = None
queue = deque()
level = 1

if tree_number_of_nodes > 0:
    root = Node(1)
    queue.append(root)
    queue.append(None)

while tree_number_of_nodes > 0 and queue:
    tmp = queue.popleft()
    if tmp is None:
        if queue:
            queue.append(None)
        level += 1
    else:
        left_node_value, right_node_value = map(int, raw_input().split(" "))
        if left_node_value != -1:
            tmp.left = Node(left_node_value)
            queue.append(tmp.left)
        if right_node_value != -1:
            tmp.right = Node(right_node_value)
            queue.append(tmp.right)
        tree_number_of_nodes -= 1

#Swaping elements from level
for swaps in xrange(int(input())):
    k = int(input())
    itr = 2
    lvl = k
    while lvl <= level:
        swap_subtree_of_level(root, lvl)
        lvl = itr * k
        itr += 1
    in_order(root)
    print ""
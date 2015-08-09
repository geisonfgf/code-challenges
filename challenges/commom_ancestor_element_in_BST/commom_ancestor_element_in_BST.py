class BinaryTree():
    def __init__(self, key, parent=None, level=0):
        self.left = None
        self.right = None
        self.key = key
        self.parent = parent
        self.level = level

    def search(self, node, key, count=0):
        count += 1
        if None == node or key == node.key:
            return node, count
        elif key < node.key:
            return node.search(node.left, key, count)
        else:
            return node.search(node.right, key, count)

    def insert(self, new_node, key, level):
        if new_node.left is None and new_node.right is None:
            if new_node.left is None:
                new_node.left = BinaryTree(key, new_node, level)
            else:
                tree = BinaryTree(key, new_node, level)
                new_node.left = tree
                tree.left = new_node.left
        elif new_node.left and new_node.right is None:
            if new_node.right is None:
                new_node.right = BinaryTree(key, new_node, level)
            else:
                tree = BinaryTree(key, new_node, level)
                tree.right = new_node.right
                new_node.right = tree

    def first_common_ancestor(self, node, first_employee, second_employee):
        manager = None
        if first_employee.level > second_employee.level:
            manager = first_employee.parent
        else:
            manager = second_employee.parent
        for i in xrange(max(first_employee.level, second_employee.level)):
            if ((manager == first_employee.parent) and
                    (first_employee.level < second_employee.level)):
                return manager.key
            elif ((manager == second_employee.parent) and
                    (first_employee.level > second_employee.level)):
                return manager.key
            if manager.parent:
                aux_manager = manager.parent
                manager = aux_manager
            
        
    def __str__(self):
        def str_helper(tree, level):
            result = ""
            if tree:
                result += str_helper(tree.right, level + 1)
                result += "| " * level
                result += tree.key + " - " + str(tree.level) + "\n"
                result += str_helper(tree.left, level + 1)
            return result
        return str_helper(self, 0)

def OutputCommonManager(count):
    first_employee, second_employee = raw_input(), raw_input()
    first_employee_node, second_employee_node = None, None
    
    for index in xrange(0, count-1):
        manager, employee = raw_input().split(" ")
        if index == 0:
            org_tree = BinaryTree(manager)
            org_tree.insert(org_tree, employee, 0)
            if first_employee == manager:
                first_employee_node = org_tree
            elif first_employee == employee:
                first_employee_node = org_tree.left
        else:
            node, level = org_tree.search(org_tree, manager)
            if node:
                node.insert(node, employee, level)
                if first_employee == node.key:
                    first_employee_node = node
                if (node.left and first_employee == node.left.key):
                    first_employee_node = node.left
                if (node.right and first_employee == node.right.key):
                    first_employee_node = node.right
                if second_employee == node.key:
                    second_employee_node = node
                if (node.left and second_employee == node.left.key):
                    second_employee_node = node.left
                if (node.right and second_employee == node.right.key):
                    second_employee_node = node.right

    print org_tree.first_common_ancestor(
        org_tree, first_employee_node, second_employee_node)

OutputCommonManager(int(input()))
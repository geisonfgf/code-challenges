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
        first_employee_manager = first_employee.parent
        second_employee_manager = second_employee.parent
        while first_employee_manager.level != second_employee_manager.level:
            if first_employee_manager.level > second_employee_manager.level:
                if first_employee_manager.parent:
                    aux_manager = first_employee_manager.parent
                    first_employee_manager = aux_manager
            else:
                if second_employee_manager.parent:
                    aux_manager = second_employee_manager.parent
                    second_employee_manager = aux_manager
        while first_employee_manager.key != second_employee_manager.key:
            if (first_employee_manager.parent and
                    second_employee_manager.parent and
                    first_employee_manager.key != second_employee_manager.key):
                aux_manager = first_employee_manager.parent
                first_employee_manager = aux_manager
                aux_manager = second_employee_manager.parent
                second_employee_manager = aux_manager
        return first_employee_manager.key

    def __str_tree_builder(self, node, level):
        str_tree = []
        if node:
            str_tree.append(self.__str_tree_builder(node.right, level + 1))
            str_tree.append("| " * level)
            str_tree.append(
                ''.join([str(node.data), " - ", str(node.level), "\n"]))
            str_tree.append(self.__str_tree_builder(node.left, level + 1))
        return ''.join(str_tree)

    def __repr__(self):
        return self.__str_tree_builder(self, 0)

def OutputCommonManager(count):
    first_employee, second_employee = raw_input(), raw_input()
    first_employee_node, second_employee_node = None, None
    
    for index in xrange(0, count-1):
        manager, employee = raw_input().split(" ")
        if index == 0:
            org_tree = BinaryTree(manager)
            org_tree.insert(org_tree, employee, 1)
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
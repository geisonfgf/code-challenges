"""
You are given as standard input the number of employees in a company, the
first names of two selected employees in a company, and the direct line
management relations between every employee. Each person in the company
can directly line manage a maximum of 2 other employees. The input has
the following format:
 
 
on the first line, the number of unique employees in the company
on the second line, the name of the first selected employee (a first name
only without spaces)
on the third line, the name of the second selected employee (a first name
only without spaces, guaranteed to be different from the first selected
employee)
on the subsequent lines, the line management relations in the format
"EmployeeX EmployeeY" - meaning EmployeeX manages EmployeeY (first names
without spaces and spaces are used to separate the two names)
 
The input is correct (there are only direct line management relations, no
cycles, all employees appear in the input).  For simplicity, the first line
after the selected employees (line 4) always contains the manager at the top
of the hierarchy.
 
Write a program that reads the input from stdin and then outputs out the name
of the single employee at the lowest point in the hierarchy to which the two
selected employees report, either directly or indirectly. If one employee
reports to the other, either directly or indirectly, print out the name of
the highest of the two selected employees.
 
Examples: 
 
Input:                  Input:                  Input:
6                       4                       5
Hilary                  Simon                   Gareth
James                   Claudiu                 Alex
Sarah Fred              Sarah Claudiu           June Alex
Sarah Paul              Sarah Paul              June Qing
Fred Hilary             Claudiu Simon           Qing Paul
Fred Jenny                                      Qing Gareth
Jenny James
 
Output:                 Output:                 Output:
Fred                    Sarah                   June
"""

class BinaryTree():
    def __init__(self, value, parent=None, level=0):
        self.left = None
        self.right = None
        self.value = value
        self.parent = parent
        self.level = level

    def search(self, node, value, count=0):
        count += 1
        if None == node or value == node.value:
            return node, count
        elif value < node.value:
            return node.search(node.left, value, count)
        else:
            return node.search(node.right, value, count)

    def insert(self, new_node, value, level):
        if new_node.left is None:
            new_node.left = BinaryTree(value, new_node, level)
        elif new_node.right is None:
            new_node.right = BinaryTree(value, new_node, level)
        else:
            tree = BinaryTree(value, new_node, level)
            tree.right = new_node.right
            new_node.right = tree

    def first_common_ancestor(self, first_employee, second_employee):
        first_employee_manager = first_employee.parent
        second_employee_manager = second_employee.parent
        while first_employee_manager.level != second_employee_manager.level:
            if first_employee_manager.level > second_employee_manager.level:
                if first_employee_manager.parent:
                    aux_manager = first_employee_manager.parent
                    first_employee_manager = aux_manager
            elif second_employee_manager.parent:
                    aux_manager = second_employee_manager.parent
                    second_employee_manager = aux_manager
        while first_employee_manager.value != second_employee_manager.value:
            if (first_employee_manager.parent and
                    second_employee_manager.parent and
                    first_employee_manager.value != second_employee_manager.value):
                aux_manager = first_employee_manager.parent
                first_employee_manager = aux_manager
                aux_manager = second_employee_manager.parent
                second_employee_manager = aux_manager
        return first_employee_manager.value

    def __str_tree_builder(self, node, level):
        str_tree = []
        if node:
            str_tree.append(self.__str_tree_builder(node.right, level + 1))
            str_tree.append("| " * level)
            str_tree.append(
                ''.join([str(node.value), " - ", str(node.level), "\n"]))
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
                if first_employee == node.value:
                    first_employee_node = node
                elif (node.left and first_employee == node.left.value):
                    first_employee_node = node.left
                elif (node.right and first_employee == node.right.value):
                    first_employee_node = node.right
                elif second_employee == node.value:
                    second_employee_node = node
                elif (node.left and second_employee == node.left.value):
                    second_employee_node = node.left
                elif (node.right and second_employee == node.right.value):
                    second_employee_node = node.right

    print org_tree
    print
    print org_tree.first_common_ancestor(first_employee_node, second_employee_node)

OutputCommonManager(int(input()))
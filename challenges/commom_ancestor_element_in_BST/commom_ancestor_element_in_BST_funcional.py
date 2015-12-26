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

class Node(object):
    """ Simple Node object """
    def __init__(self, value, parent=None, level=0):
        self.left = None
        self.right = None
        self.value = value
        self.parent = parent
        self.level = level

def binary_search(node, value):
    """Perform a binary search in a tree of nodes.
    
    Args:
        :param node (Node): Node object where search will be started.
        :param value (String): value to be found.
    
    Returns:
        Node: Node found or None otherwise
    """
    aux_node = None
    while node is not None and node.value != value:
        if value < node.value:
            aux_node = node.left
            node = aux_node
        else:
            aux_node = node.right
            node = aux_node
    return node if node.value == value else None

def insert_node_in_tree(current_node, value):
    """Insert a new node in a tree.
    
    Args:
        :param current_node (Node): Node object where will be inserted
                                    the new node.
        :param value (String): value to be inserted.
    """
    current_node_level = get_node_level(current_node)
    if current_node.left is None:
        current_node.left = Node(value, current_node, current_node_level + 1)
    elif current_node.right is None:
        current_node.right = Node(value, current_node, current_node_level + 1)
    else:
        new_node = Node(value, current_node, current_node_level + 2)
        current_node.right = new_node
        new_node.right = current_node.right

def get_node_level(node):
    """Get the level of a node in a tree.
    
    Args:
        :param node (Node): Node object which will be get the level.
    
    Returns:
        int: level of the Node passed in Args
    """
    level, aux_node = 0, None
    while node.parent is not None:
        aux_node = node.parent
        node = aux_node
        level += 1
    return level

def get_common_ancestor_of_nodes(node_a, node_b):
    """Discover the common ancestor node of two nodes in a tree.
    
    Args:
        :param node_a (Node): Node object.
        :param node_b (Node): Node object.
    
    Returns:
        String: The value of common ancestor of two nodes
    """
    while node_a.parent.level != node_b.parent.level:  # even parent level
        if node_a.parent.level > node_b.parent.level and node_a.parent.parent:
            aux_node = node_a.parent.parent
            node_a.parent = aux_node
        elif node_b.parent.parent:
            aux_node = node_b.parent.parent
            node_b.parent = aux_node
    while node_a.parent.value != node_b.parent.value:
        if (node_a.parent.parent and node_b.parent.parent and
                node_a.parent.value != node_b.parent.value):
            aux_node = node_a.parent.parent
            node_a.parent = aux_node
            aux_node = node_b.parent.parent
            node_b.parent = aux_node
    return node_a.parent.value

def print_node_tree(node, level=0):
    """Print a representation of tree in STDOUT.
    
    Args:
        :param node (Node): Node object.
    """
    str_builder = []
    if node:
        str_builder.append(print_node_tree(node.right, level + 1))
        str_builder.append("| " * level)
        str_builder.append(
            ''.join([str(node.value), " - ", str(node.level), "\n"]))
        str_builder.append(print_node_tree(node.left, level + 1))
    return ''.join(str_builder)

def OutputCommonManager(count):
    first_employee, second_employee = raw_input(), raw_input()
    first_employee_node, second_employee_node = None, None
    for index in xrange(0, count-1):
        manager, employee = raw_input().split(" ")
        if index == 0:
            org_tree = Node(manager)
            insert_node_in_tree(org_tree, employee)
            if first_employee == manager:
                first_employee_node = org_tree
            elif first_employee == employee:
                first_employee_node = org_tree.left
        else:
            node = binary_search(org_tree, manager)
            if node:
                insert_node_in_tree(node, employee)
                if first_employee == node.value:
                    first_employee_node = node
                elif node.left and first_employee == node.left.value:
                    first_employee_node = node.left
                elif node.right and first_employee == node.right.value:
                    first_employee_node = node.right
                elif second_employee == node.value:
                    second_employee_node = node
                elif node.left and second_employee == node.left.value:
                    second_employee_node = node.left
                elif node.right and second_employee == node.right.value:
                    second_employee_node = node.right
    print get_common_ancestor_of_nodes(first_employee_node,
                                       second_employee_node)
    print '\n', print_node_tree(org_tree)

if __name__ == '__main__':
    OutputCommonManager(int(input()))

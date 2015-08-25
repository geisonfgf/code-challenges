class Trie(object):

    class Node(object):

        def __init__(self):
            self.left = None
            self.mid = None
            self.right = None
            self.val = None
            self.c = None
  
    def __init__(self):
        self.root = None
        self.size = 0

    def contains(self, key):
        return self.get_value(key) != None

    def get_value(self, key):
        if key is None:
            raise LookupError("Key could not be null.")
        if len(key) == 0:
            raise LookupError("Key could not be empty.")
        node = self.get_node(self.root, key, 0)
        if node is None:
            return None
        return node.val

    def get_node(self, node, key, d):
        if key is None:
            raise LookupError("Key could not be null.")
        if len(key) == 0:
            raise LookupError("Key could not be empty.")
        if node is None:
            return None
        c = key[d]
        if c < node.c:
            return self.get_node(node.left, key, d)
        elif c > node.c:
            return self.get_node(node.right, key, d)
        elif d < len(key) - 1:
            return self.get_node(node.mid, key, d + 1)
        else:
            return node

    def put(self, key, val):
        if not self.contains(key):
            self.size += 1
        self.root = self.__put(self.root, key, val, 0)

    def __put(self, node, key, val, d):
        c = key[d]
        if node is None:
            node = Trie.Node()
            node.c = c
        if c < node.c:
            node.left = self.__put(node.left, key, val, d)
        elif c > node.c:
            node.right = self.__put(node.right, key, val, d)
        elif d < len(key) - 1:
            node.mid = self.__put(node.mid, key, val, d + 1)
        else:
            node.val = val
        return node

    def longest_prefix_of(self, query):
        if query is None or len(query) == 0:
            return None
        length, i = 0, 0
        node = self.root
        while node and i < len(query):
            c = query[i]
            if c < node.c:
                node = node.left
            elif c > node.c:
                node = node.right
            else:
                i += 1
                if node.val:
                    length = i
                node = node.mid
        return query[:length]

    def keys(self):
        queue = []
        self.collect(self.root, [], queue)
        return queue

    def keys_with_prefix(self, prefix):
        queue = []
        node = self.get_node(self.root, prefix, 0)
        if node is None:
            return queue
        if node.val:
            queue.append(prefix)
        self.collect(node.mid, [prefix], queue)
        return queue

    def keys_that_match(self, pattern):
        queue = []
        self.collect_nodes(root, [], 0, pattern, queue)
        return queue

    def collect(self, node, prefix, queue):
        if node is None:
            return
        self.collect(node.left, prefix, queue)
        if node.val:
            queue.append(''.join(prefix) + node.c)
        self.collect(node.mid, prefix + [node.c], queue)
        self.collect(node.right, prefix, queue)

    def collect_nodes(self, node, prefix, i, pattern, queue):
        if node is None:
            return
        c = pattern[i]
        if c == '.' or c < node.c:
            self.collect_nodes(node.left, prefix, i, pattern, queue)
        if node == '.' or c == node.c:
            if i == len(pattern) - 1 and node.val:
                queue.append(''.join(prefix) + node.c)
            if i < len(pattern) - 1:
                self.collect_nodes(
                    node.mid, prefix + [node.c], i + 1, pattern, queue)
        if c == '.' or c > node.c:
            self.collect_nodes(node.right, prefix, i, pattern, queue)
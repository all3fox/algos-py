class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.lft, self.rgt = None, None

    def get_node_with_parent(self, key):
        parent = None
        while self:
            if key == self.key:
                return self, parent

            if key < self.key:
                self, parent = self.lft, self
            else:
                self, parent = self.rgt, self

        return None, parent

    def get(self, key):
        node, _ = self.get_node_with_parent(key)
        return None if node is None else node.val


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def get_node_with_parent(self, key):
        if self.root is None: return None, None
        return self.root.get_node_with_parent(key)

    def get(self, key):
        if self.root is None: return None
        return self.root.get(key)

    def put(self, key, val):
        node, parent = self.get_node_with_parent(key)

        if node is None and parent is None:
            self.root = Node(key, val)
        elif node is None:
            if key < parent.key:
                parent.lft = Node(key, val)
            else:
                parent.rgt = Node(key, val)
        else:
            node.val = val

    def remove(self, key):
        node, parent = self.get_node_with_parent(key)

        if node is None: return # no such key or empty tree

        if node.lft and node.rgt:
            heir, parent = node.lft, node
            while heir.rgt:
                heir, parent = heir.rgt, heir
            if parent is node:
                parent.lft = heir.lft
            else:
                parent.rgt = heir.lft
            node.key, node.val = heir.key, heir.val
        elif node.lft:
            heir = node.lft
            node.key, node.val = heir.key, heir.val
            node.lft, node.rgt = heir.lft, heir.rgt
        elif node.rgt:
            heir = node.rgt
            node.key, node.val = heir.key, heir.val
            node.lft, node.rgt = heir.lft, heir.rgt
        else:
            if node is self.root:
                self.root = None
            else:
                if node is parent.lft:
                    parent.lft = None
                else:
                    parent.rgt = None
            heir = node

        heir.key, heir.val = None, None
        heir.lft, heir.rgt = None, None

    def __contains__(self, key):
        return True if self.get(key) is not None else False

    def __setitem__(self, key, val):
        return self.put(key, val)

    def __getitem__(self, key):
        return self.get(key)
"""
Naive implementation of the binary search tree

See: https://en.wikipedia.org/wiki/Binary_search_tree
"""


class BinarySearchTree:
    """
    Naive implementation of the binary search tree
    """
    class Node:
        """
        Single node of the binary search tree
        """
        def __init__(self, key, val):
            self.key, self.val = key, val
            self.lft, self.rgt = None, None

    def __init__(self):
        self.root = None

    def get_node_with_parent(self, key):
        """
        Find the node which holds the key, and return the node and its parent

        If no such node is present in the tree, return only the parent node.
        This parent node can be used to attach a new node that holds the key.
        """
        node, parent = self.root, None

        while node:
            if key == node.key:
                return node, parent

            if key < node.key:
                node, parent = node.lft, node
            else:
                node, parent = node.rgt, node

        return None, parent

    def get(self, key):
        """
        Find the node which holds the key, and return the attached value

        If no such node exists in the tree, return None
        """
        node, _ = self.get_node_with_parent(key)
        return None if node is None else node.val

    def put(self, key, val):
        """
        Put the (key, val) pair as a node into the tree

        If a node which holds the key already exists, overwrite its value
        """
        node, parent = self.get_node_with_parent(key)

        if node is None and parent is None:
            self.root = self.Node(key, val)
        elif node is None:
            if key < parent.key:
                parent.lft = self.Node(key, val)
            else:
                parent.rgt = self.Node(key, val)
        else:
            node.val = val

    def remove(self, key):
        """
        Remove the node which holds the key from the tree

        If no such node exists in the tree, do nothing
        """
        node, parent = self.get_node_with_parent(key)

        if node is None:
            return  # no such key or empty tree

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
        return self.get(key) is not None

    def __setitem__(self, key, val):
        return self.put(key, val)

    def __getitem__(self, key):
        return self.get(key)

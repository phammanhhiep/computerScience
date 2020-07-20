import os, sys, math, logging

from elementaryDataStructures_10 import stack, linkedlist


logging.basicConfig(filename="binarySearchTree.log", level=logging.DEBUG)


class BinarySearchTree:
    def __init__(self, root_node):
        """
        Assume the tree has the binary-search-tree property at the beginning. 
        """
        self.root_node = root_node


    def get_predecessor(self, node): pass


    def get_successor(self, node):
        """
        Assume keys are distinct. To handle non-distinct keys, the function need
        someway to compare two nodes. 
        """ 
        if node.has_right():
            return self.get_minimum(node.get_right())
        
        p = node.get_parent()

        while p is not None and (p.get_right() is not None and node.key == p.get_right().key):
            node = p.get_right()
            p = p.get_parent()
        return p


    def get_minimum(self, node):
        while node.has_left():
            node = node.get_left()
        return node


    def inode_tree_walk(self):
        # Nonrecursive version
        s = stack.Stack(100)
        a = []
        root_node = self.root_node
        while root_node is not None:
            if root_node.has_right():
                s.push(root_node.get_right())
            s.push(root_node)
            if root_node.has_left():
                left = root_node.get_left()
                s.push(left)
                root_node = left
            else:
                a.append(root_node.get_key())
                try:
                    s.pop()
                    root_node = s.pop()
                except Exception as e:
                    logging.debug("Stack is empty. Set root as None.")
                    root_node = None
        return a


    def inode_tree_walk2(self):
        min_node = self.get_minimum(self.root_node)
        suc_node = self.get_successor(min_node)
        a = [min_node.get_key()]

        while suc_node is not None:
            a.append(suc_node.get_key())
            suc_node = self.get_successor(suc_node)
        return a


    def insert(self, node, root_node=None):
        """
        Recursive version.
        """
        if root_node is None:
            root_node = self.root_node
        if self.root_node is None:
            self.root_node = node
        else:
            has_left = root_node.has_left()
            has_right = root_node.has_right()
            if root_node.key > node.key and not has_left:
                root_node.set_relative(1, node)
                node.set_relative(3, root_node)
            elif root_node.key > node.key and has_left:
                self.insert(node, root_node.get_left())
            elif root_node.key <= node.key and not has_right:
                root_node.set_relative(1, node)
                node.set_relative(3, root_node)
            elif root_node.key <= node.key and has_right:
                self.insert(node, root_node.get_right())


    def postorder_tree_walk(root_node): pass
        # Nonrecursive version


    def preorder_tree_walk(root_node): pass 
        # Nonrecursive version



import logging

from elementaryDataStructures_10.linkedlist import Node as OriginalNode
from binarySearchTrees_12.binarySearchTree import BinarySearchTree


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class NilNode(OriginalNode):
    def __init__(self, key=None, left=None, right=None, parent=None):
        OriginalNode.__init__(self, key, left, right, parent)
        self.BLACK = 1    
        self.RED = 2   
        self.color = self.BLACK


    def get_color(self):
        return self.color


    def set_black(self):
        self.color = self.BLACK


    def set_red(self):
        logging.error("NIL cannot be set as red")
        raise ValueError()


    def set_color(self, color):
        if self.BLACK == color:
            self.set_black()
        elif self.RED == color:
            self.set_red()
        else:
            logging.error("{} is not a color".format(color)) 
            raise ValueError()


    def is_black(self):
        return True


class Node(NilNode):
    """
    Color: 1 for red and 2 for black.
    """
    def __init__(self, key, color=None, left=None, right=None, parent=None):
        NilNode.__init__(self, key, left, right, parent)
        if self.left is None:
            self.left = NilNode()
        if self.right is None:
            self.right = NilNode()
        if self.parent is None:
            self.parent = NilNode() 
        self.color = color if color is not None else self.BLACK


    def set_red(self):
        self.color = self.RED


    def is_black(self):
        if self.color == self.RED:
            return False
        else:
            return True


    def has_left(self):
        if self.get_left().get_key() is not None:
            return True
        else:
            return False

    def has_right(self):
        if self.get_right().get_key() is not None:
            return True
        else:
            return False


    def has_parent(self):
        if self.get_parent().get_key() is not None:
            return True
        else:
            return False            

class RedBlackTree(BinarySearchTree):
    """
    Assuming keys are distinct.
    """
    def __init__(self, root_node=None):
        BinarySearchTree.__init__(self, root_node)
        if root_node is not None:
            root_node.set_black()


    def right_rotate(self, node):
        if not node.has_left():
            logging.error("Node has no left child")
            raise ValueError()

        left = node.get_left()
        left.set_parent(node.get_parent())

        if not node.has_parent():
            self.root_node = left
        elif node.get_parent().has_left() and node.get_parent().get_left().equal_to(node):
            node.get_parent().set_left(left)
        else:
            node.get_parent().set_right(left)
        
        node.set_left(left.get_right())
        node.set_parent(left)
        left.set_right(node)

        if node.has_left():
            node.get_left().set_parent(node) 


    def left_rotate(self, node):
        if not node.has_right():
            logging.error("Node has no right child")
            raise ValueError()

        right = node.get_right()
        right.set_parent(node.get_parent())

        if not node.has_parent():
            self.root_node = right
        elif node.get_parent().has_left() and node.get_parent().get_left().get_key() == node.get_key():
            node.get_parent().set_left(right)
        else:
            node.get_parent().set_right(right)
        
        node.set_right(right.get_left())
        node.set_parent(right)
        right.set_left(node)

        if node.has_right():
            node.get_right().set_parent(node) 


    def insert(self): pass


    def insert_fixup(self): pass


    def delete(self):
        pass


    def delete_fixup(self, x):
        while not x.equal_to(self.root_node) and x.is_black():
            xp =  x.get_parent()
            if xp.has_left_as(x):
                logging.debug("Node({}) is the left child".format(x.get_key()))
                w = xp.get_right()
                if not w.is_black():
                    logging.debug("Case 1: The sibling of the Node({}) is red"
                        .format(x.get_key()))
                    w.set_black()
                    xp.set_red()
                    self.left_rotate(xp)
                    w = xp.get_right()
                if w.get_left().is_black() and w.get_right().is_black():
                    logging.debug("Case 2: The left and right children of the sibling of the Node({}) are black".format(x.get_key()))
                    w.set_red()
                    x = x.get_parent()
                elif w.get_right().is_black():
                    logging.debug("Case 3: The right children of the sibling of the Node({}) is black, but not the left child".format(x.get_key()))
                    w.get_left().set_black()
                    w.set_red()
                    self.right_rotate(w)
                    w = xp.get_right()
                else:
                    logging.debug("Case 4: The right children of the sibling of the Node({}) is red".format(x.get_key()))     
                    w.set_color(xp.get_color())
                    xp.set_black()
                    w.get_right().set_black()
                    self.left_rotate(xp)
                    x = self.root_node              
            else:
                logging.debug("Node({}) is the right child".format(x.get_key()))
                w = xp.get_left()
                if not w.is_black():
                    logging.debug("Case 1: the sibling of the parent of the Node({}) is red".format(x.get_key()))
                    w.set_black()
                    xp.set_red()
                    self.right_rotate(xp)
                    w = xp.get_left()
                if w.get_left().is_black() and w.get_right().is_black():
                    logging.debug("Case 2: The left and right children of the sibling of the Node({}) are black".format(x.get_key()))
                    w.set_red()
                    x = x.get_parent()
                elif not w.get_right().is_black():
                    logging.debug("Case 3: The right children of the sibling of Node({}) is red".format(x.get_key()))
                    w.get_right().set_black()
                    w.set_red()
                    self.left_rotate(w)
                    w = xp.get_right()
                else:
                    logging.debug("Case 4: The right child is black of the sibling of Node({})".format(x.get_key()))     
                    w.set_color(xp.get_color())
                    xp.set_black()
                    w.get_left().set_black()
                    self.right_rotate(xp)
                    x = self.root_node
        x.set_black()


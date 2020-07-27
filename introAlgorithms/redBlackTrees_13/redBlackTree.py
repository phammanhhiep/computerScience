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


    def is_nil(self):
        logging.debug("Check if node({}) is NIL".format(self.get_key()))
        if self.is_black() and self.get_key() is None:
            return True
        elif self.get_key() is not None:
            return False
        else:
            logging.error("Nondetermined node")
            raise ValueError()


    def equal_to(self, x):
        if self.is_nil() and x.is_nil():
            return True
        elif not x.is_nil() and not self.is_nil():
            if self.get_key() == x.get_key():
                return True
            else:
                return False
        else:
            False         


class Node(NilNode):
    """[summary]
    
    Every node has a left and right children. By defaut, they are NilNode.
    
    Extends:
        NilNode
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
    """[summary]
    
    Assuming keys are distinct.
    
    Extends:
        BinarySearchTree
    """
    def __init__(self, root_node=None):
        if root_node is None:
            root_node = NilNode()
        BinarySearchTree.__init__(self, root_node)
        if root_node is not None:
            logging.info("Set the color of root as black")
            root_node.set_black()


    def get_minimum(self, node=None):
        """[summary]
        
        The function assumes,
        - Either node is not provided or node must be an instance of Node. 
        - Provided node must always has both left and right children.

        The return node must be an internal nodes, because we choose to order them by their keys.
        
        Keyword Arguments:
            node {[type]} -- [description] (default: {None})
        """
        if node is None:
            node = self.root_node
        if not node.has_parent() and (node.get_key() is None):
            logging.error("Empty tree is provided")
            raise ValueError

        x = node    
        while node.get_key() is not None:
            logging.debug("Node({}) is checking".format(node.get_key()))
            x = node
            node = node.get_left()
        logging.debug("Minimum node ({})".format(x.get_key()))
        return x


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


    def transplant(self, u, v):
        """Replace node u by node v, but not handle the positions of children of v
        
        [description]
        
        Arguments:
            u {[type]} -- [description]
            v {[type]} -- [description]
        """
        parent = u.get_parent()

        if not u.has_parent():
            self.root_node = u
        elif parent.has_right_as(u):
            parent.set_right(v)
        else:
            parent.set_left(v)

        v.set_parent(parent)


    def insert(self): pass


    def insert_fixup(self): pass


    def delete(self, z):
        """Delete node z from the tree.
        
        [description]
        
        Arguments:
            z {[type]} -- [description]
        """
        y = z
        y_original_color = y.get_color()

        if not z.has_left():
            x = z.get_right()
            self.transplant(z, x)
        elif not z.has_right():
            x = z.get_left()
            self.transplant(z, x)
        else:
            y = self.get_minimum(z.get_right())
            y_original_color = y.get_color()
            x = y.get_right()
            if y.has_parent_as(z):
                x.set_parent(y)
            else:
                self.transplant(y, x)
                y.set_right(z.get_right())
                y.get_right().set_parent(y)
            self.transplant(z, y)
            y.set_left(z.get_left())
            y.get_left().set_parent(y)
            y.set_color(z.get_color())

        if self.root_node.BLACK == y_original_color:
            self.delete_fixup(x)



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


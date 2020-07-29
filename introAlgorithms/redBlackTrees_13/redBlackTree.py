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
        if self.get_left() is None:
            self.set_left(NilNode())
        if self.get_right() is None:
            self.set_right(NilNode())
        if self.get_parent() is None:
            self.set_parent(NilNode()) 
        self.color = color if color is not None else self.color


    def set_red(self):
        self.color = self.RED


    def is_black(self):
        if self.color == self.RED:
            return False
        else:
            return True


    def is_red(self):
        if self.is_black():
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


class AugmentedNilNode(NilNode):
    def __init__(self, key=None, left=None, right=None, parent=None):
        NilNode.__init__(self, key, left, right, parent)
        self.size = 0


    def get_size(self):
        return self.size


    def set_size(self, n):
        self.size = n


class AugmentedNode(Node):
    """A node with additional attributes
    
    [description]
    
    Extends:
        Node
    """
    def __init__(self, key, color=None, left=None, right=None, parent=None, size=1):
        Node.__init__(self, key, color, left, right, parent)
        self.size = size
        if self.get_left().is_nil():
            self.set_left(AugmentedNilNode())
        if self.get_right().is_nil():
            self.set_right(AugmentedNilNode())
        if self.get_parent().is_nil():
            self.set_parent(AugmentedNilNode())


    def get_size(self):
        return self.size


    def set_size(self, n):
        self.size = n


class RedBlackTree(BinarySearchTree):
    """[summary]
    
    Assumptions,
    - Keys are distinct
    
    Extends:
        BinarySearchTree
    """
    def __init__(self, root_node=None):
        if root_node is None:
            root_node = NilNode()
        BinarySearchTree.__init__(self, root_node)
        if root_node is not None:
            logging.debug("Set the color of root as black")
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
            x = node
            node = node.get_left()
        logging.debug("Minimum node ({})".format(x.get_key()))
        return x


    def get_successor(self, node):
        """
        Assume keys are distinct. To handle non-distinct keys, the function need
        someway to compare two nodes. 
        """ 
        if node.has_right():
            return self.get_minimum(node.get_right())
        
        p = node.get_parent()

        while not p.is_nil() and p.get_right().equal_to(node):
            node = p
            p = p.get_parent()
            logging.debug("Node: {}, parent: {}".format(node.get_key(), p.get_key()))
        return p


    def inorder_tree_walk(self, color=False):
        min_node = self.get_minimum(self.root_node)
        suc_node = self.get_successor(min_node)
        if color is True:
            a = [(min_node.get_key(), min_node.get_color())]
        else:
            a = [min_node.get_key()]

        while not suc_node.is_nil():
            logging.debug("suc_node: {}".format(suc_node.get_key()))
            if color is True:
                a.append((suc_node.get_key(), suc_node.get_color()))
            else:
                a.append(suc_node.get_key())
            suc_node = self.get_successor(suc_node)
        return a


    def right_rotate(self, node):
        if not node.has_left():
            logging.error("Node has no left child")
            raise ValueError()

        left = node.get_left()
        logging.debug("Right rotate node({}) and node({})".format(node.get_key(), left.get_key()))
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
        logging.debug("Left rotate node({}) and node({})".format(node.get_key(), right.get_key()))
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


    def insert(self, z):
        x = self.root_node
        while not x.is_nil():
            y = x
            if z.get_key() < x.get_key():
                x = x.get_left()
            else:
                x = x.get_right()
        z.set_parent(y)

        if y.is_nil():
            self.root_node = z
        elif z.get_key() < y.get_key():
            y.set_left(z)
        else:
            y.set_right(z)

        z.set_red()
        logging.debug("Insert node({}) as child of node({})".format(z.get_key(), y.get_key()))
        self.insert_fixup(z)


    def insert_fixup(self, z):
        while not z.get_parent().is_black():
            zp = z.get_parent()
            if zp.get_parent().has_left_as(zp):
                logging.debug("The parent of node({}) is left child".format(z.get_key()))
                y = zp.get_parent().get_right()
                if not y.is_black():
                    logging.debug("Case 1: The uncle of node({}) is red".format(z.get_key()))
                    zp.set_black()
                    y.set_black()
                    zp.get_parent().set_red()
                    z = zp.get_parent()
                elif zp.has_right_as(z):
                    logging.debug("Case 2: The uncle of node({}) is black and the node is the right child".format(z.get_key()))
                    z = zp
                    self.left_rotate(z)
                else:
                    logging.debug("Case 3: The uncle of node({}) is black and the node is the left child".format(z.get_key()))
                    zp.set_black()
                    zp.get_parent().set_red()
                    self.right_rotate(zp.get_parent())
            else:
                logging.debug("The parent of node({}) is right child".format(z.get_key()))
                y = zp.get_parent().get_left()
                if not y.is_black():
                    logging.debug("Case 1: If uncle of node({}) is red".format(z.get_key()))
                    zp.set_black()
                    y.set_black()
                    zp.get_parent().set_red()
                    z = zp.get_parent()
                elif zp.has_left_as(z):
                    logging.debug("Case 2: If uncle of node({}) is black and the node is the left child".format(z.get_key()))
                    z = zp
                    self.right_rotate(z)
                else:
                    logging.debug("Case 3: If uncle of node({}) is black and the node is the right child".format(z.get_key()))
                    zp.set_black()
                    zp.get_parent().set_red()
                    self.left_rotate(zp.get_parent())
        self.root_node.set_black()


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


class AugmentedRBTree(RedBlackTree):
    def __init__(self, root_node=None):
        if root_node is None:
            root_node = AugmentedNilNode()
        RedBlackTree.__init__(self, root_node)
        self.maintain_size()


    def maintain_size(self, x=None):
        """Maintain the size of a subtree whose root is the given node
        
        [description]
        
        Keyword Arguments:
            x {[type]} -- [description] (default: {None})
        """ 
        if x is None:
            x = self.root_node
        if x.is_nil():
            return x.get_size()
        else:
            ls = self.maintain_size(x.get_left())
            rs = self.maintain_size(x.get_right())
            s = ls + rs + 1
            x.set_size(s)
            return s


    def select_by_rank(self, i, x=None):
        """Return a node with rank within the tree rooted at x 
        
        [description]
        
        Arguments:
            i {[type]} -- [description]
        
        Keyword Arguments:
            x {[type]} -- [description] (default: {None})
        """
        if x is None:
            x = self.root_node
        r = x.get_left().get_size() + 1
        if i == r:
            return x
        elif i < r:
            return self.select_by_rank(i, x.get_left())
        else:
            return self.select_by_rank(i-r, x.get_right())


    def get_rank(self, x):
        """Return rank of a node
        
        [description]
        
        Arguments:
            x {[type]} -- [description]
        """ 
        r = x.get_left().get_size() + 1
        y = x

        while not y.equal_to(self.root_node):
            yp = y.get_parent()
            if yp.has_right_as(y):
                r = r + yp.get_left().get_size() + 1
            y = yp
        return r


    def right_rotate(self, x):
        """Rotate and update sizes
        
        [description]
        
        Arguments:
            x {[type]} -- [description]
        """ 
        left = x.get_left()
        ori_size = x.get_size()
        root_original_color = self.root_node.get_color()

        rb = RedBlackTree(self.root_node)
        rb.root_node.set_color(root_original_color)

        rb.right_rotate(x)
        if rb.root_node.equal_to(left):
            self.root_node = left
        left.set_size(ori_size)
        x.set_size(x.get_left().get_size() + x.get_right().get_size() + 1)


    def left_rotate(self, x):
        """Left rotate and update sizes
        
        The creation of a red-black tree could reset root color, which may be not desired when the method is called in the insert method. That is why we need to keep the orginal color of the root and set it after the creation.
        
        Arguments:
            x {[type]} -- [description]
        """ 

        right = x.get_right()
        ori_size = x.get_size()
        root_original_color = self.root_node.get_color()

        rb = RedBlackTree(self.root_node)
        rb.root_node.set_color(root_original_color)

        rb.left_rotate(x)
        if rb.root_node.equal_to(right):
            self.root_node = right
        right.set_size(ori_size)
        x.set_size(x.get_left().get_size() + x.get_right().get_size() + 1)


    def insert(self, z):
        """Insert a node and also update ranks
        
        [description]
        
        Arguments:
            z {[type]} -- [description]
        """ 
        x = self.root_node
        y = AugmentedNilNode()

        while not x.is_nil():
            y = x
            y.set_size(y.get_size() + 1)
            if z.get_key() < x.get_key():
                x = x.get_left()
            else:
                x = x.get_right()
        z.set_parent(y)

        if y.is_nil():
            self.root_node = z
        elif z.get_key() < y.get_key():
            y.set_left(z)
        else:
            y.set_right(z)

        z.set_red()
        logging.debug("Insert node({}) as child of node({})".format(z.get_key(), y.get_key()))
        self.insert_fixup(z)


    def delete(self, z):
        """Delete a node and update size
        
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
            y.set_size(z.get_size())

        k = x    
        while not k.get_parent().is_nil():
            kp = k.get_parent()
            kp.set_size(kp.get_size() - 1)
            k = kp

        if self.root_node.BLACK == y_original_color:
            self.delete_fixup(x)


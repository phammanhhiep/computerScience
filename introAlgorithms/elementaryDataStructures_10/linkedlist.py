import logging


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class Node():
    def __init__(self, key=None, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent


    def set_key(self, key):
        self.key = key


    def set_relative(self, id, x):
        if id == 1: 
            self.left = x
        elif id == 2:
            self.right = x
        else:
            self.parent = x


    def set_left(self, x):
        self.left = x
        x.set_parent(self)


    def set_right(self, x):
        self.right = x
        x.set_parent(self)


    def set_parent(self, x):
        self.parent = x


    def rm_relative(self, id):
        if id == 1: 
            self.left = None
        elif id == 2:
            self.right = None
        else:
            self.parent = None    


    def rm_left(self):
        self.left = None


    def rm_right(self):
        self.right = None


    def rm_parent(self):
        self.parent = None


    def has_right(self):
        if self.right is not None:
            return True
        else: 
            return False


    def has_left(self):
        if self.left is not None:
            return True
        else: 
            return False

    def has_parent(self):
        if self.parent is not None:
            return True
        else: 
            return False        

            
    def get_key(self):
        return self.key


    def get_right(self):
        return self.right


    def get_left(self):
        return self.left


    def get_parent(self):
        return self.parent


    def has_left_as(self, x):
        """
        Check if node x is the left child of the object
        """
        if self.has_left() and (self.get_left().equal_to(x)):
            return True
        else:
            return False


    def has_right_as(self, x):
        if self.has_right() and (self.get_right().equal_to(x)):
            return True
        else:
            return False


    def has_parent_as(self, x):
        if self.has_parent() and (self.get_parent().equal_to(x)):
            return True
        else:
            return False


    def equal_to(self, x):
        if self.get_key() == x.get_key():
            return True
        else:
            return False


class DoublyList:
    def __init__(self): pass

    def next(self): pass


class SinglyList: pass



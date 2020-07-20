class Node():
    def __init__(self, key=None, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent


    def set_key(self, key):
        self.key = key


    def set_relative(self, id, obj):
        if id == 1: 
            self.left = obj
        elif id == 2:
            self.right = obj
        else:
            self.parent = obj


    def set_left(self, obj):
        self.left = obj


    def set_right(self, obj):
        self.right = obj


    def set_parent(self, obj):
        self.parent = obj


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



class DoublyList:
    def __init__(self): pass

    def next(self): pass


class SinglyList: pass



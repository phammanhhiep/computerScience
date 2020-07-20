import logging

from elementaryDataStructures_10.linkedlist import Node as OriginalNode
from binarySearchTrees_12.binarySearchTree import BinarySearchTree


logging.basicConfig(filename="redBlackTree.log", level=logging.DEBUG)


class Node(OriginalNode):
	"""
	Color: 1 for red and 2 for black.
	"""
	def __init__(self, key=None, color=None, left=None, right=None, parent=None):
		OriginalNode.__init__(self, key, left, right, parent)
		self.BLACK = 1
		self.RED = 2		
		self.color = color


	def set_black(self):
		self.color = self.BLACK


	def set_red(self):
		self.color = self.RED


class RedBlackTree(BinarySearchTree):
	"""
	Assuming keys are distinct.
	"""
	def __init__(self, root_node=None):
		BinarySearchTree.__init__(self, root_node)


	def right_rotate(self, node):
		if not node.has_left():
			logging.error("Node has no left child")
			raise ValueError()

		left = node.get_left()

		if not node.has_parent():
			self.root_node = left
		elif node.get_parent().has_left() and node.get_parent().get_left().get_key() == node.get_key():
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


	def delete(self): pass


	def delete_fixup(self): pass


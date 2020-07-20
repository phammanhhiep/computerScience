import logging

from elementaryDataStructure_10.linkedlist import Node
from binarySearchTrees_12.binarySearchTree import BinarySearchTree


logging.basicConfig(filename="redBlackTree.log", level=logging.DEBUG)


class Node2(Node):
	"""
	Color: 1 for red and 2 for black.
	"""
	def __init__(self, key=None, color=None, left=None, right=None, parent=None):
		Node.__init__(self, key, left, right, parent)
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
			logging.warning("Node has no left child")
		left = node.get_left()

		left.set_relative(node.get_parent(), 3)

		if not node.has_parent():
			self.root_node = left
		elif node.get_parent().has_left() and node.get_parent().get_left().get_key() == node.get_key():
			node.get_parent().set_relative(left, 1)
		else:
			node.get_parent().set_relative(left, 2)
		
		node.set_relative(left, 2)
		node.set_relative(left.get_right(), 1)
		left.set_relative(node, 2)


	def left_rotate(self, node):
		pass
def bfs (s):
	'''
	Traverse the graph g from the source node s to build a breadth-first tree
	'''
	s.set_distance ()
	queue = [s]
	while len (queue) > 0:
		u = queue.pop ()
		u.set_black ()
		for n in u.neighbors ():
			if n.is_white ():
				n.set_parent (u)
				n.set_grey ()
				n.set_distance ()
				queue.insert (0, n)

def shortest_path (s, v):
	'''
	Traverse the breadth-first tree and return node in the shortest path.
	'''
	cur = v
	p = []
	while cur is not None:
		p.insert(0, cur)
		cur = cur.parent ()
	return p

def create_nodes (num):
	return [Node () for i in range (num)]

class Node:
	'''
	Represent a node of an undirected graph 
	'''
	WHITE = 1
	BLACK = 2
	GREY = 3

	def __init__ (self):
		self._neighbors = []
		self._cur_nb_index = 0
		self._distance = None
		self._parent = None
		self._color = self.WHITE

	def set_grey (self):
		self._color = self.GREY

	def set_black (self):
		self._color = self.BLACK

	def is_white (self):
		if self._color == self.WHITE: 
			return True
		else:
			return False

	def is_black ():
		if self._color == self.BLACK: 
			return True
		else:
			return False

	def is_grey ():
		if self._color == self.GREY: 
			return True
		else:
			return False		

	def connect (self, n):
		self._add_neighbor (n)
		n._add_neighbor (self)

	def _add_neighbor (self, n):
		self._neighbors.append (n)

	def set_parent (self, p):
		self._parent = p

	def parent (self):
		return self._parent

	def set_distance (self, val=0):
		if self.parent ():
			self._distance = self.parent ().distance () + 1
		else:
			self._distance = 0

	def distance (self):
		return self._distance

	def neighbors (self):
		return self._neighbors

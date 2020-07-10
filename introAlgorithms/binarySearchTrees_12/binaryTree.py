class BinaryTree:
	def getRoot(self): pass


	def getLeft(self, n): pass


	def getSibling(self, n): pass


	def getParent(self, n): pass


	def getKey(self, n): pass


	def traverseBinaryTree(self):
		r = self.getRoot()
		s = False # indicator of whether the procedure start
		while self.getParent(r) is not None or s is False:
			l = self.getLeft(r)
			sib = self.getSibling(l)
			if l is not None:
				s = True
				print(self.getKey(l))
				if sib is not None:
					print(self.getKey(sib))
				r = l
			# ON GOING


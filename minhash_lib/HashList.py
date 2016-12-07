
from HashSet import *

import sys 

from math import log

# List for Hash
# Push_back

class HashList:
	def __init__(self, maxSizeOfHashList = 10):
		# the size of hash table for all kmers
		self.maxSizeOfHashList = maxSizeOfHashList

		self.hashList = []
		self.hashSet = HashSet()

	def sizeOfList(self):
		return len(self.hashList)

	def updateHashSet(self):
		self.hashSet.getList(self.hashList)

	def add(self, value):

		if len(self.hashList) >= self.maxSizeOfHashList and value > self.hashList[-1]:
			return

		self.hashSet.insertNewValue(value)
		self.hashList = self.hashSet.toHashList()

		if self.sizeOfList() > self.maxSizeOfHashList:
			self.hashList = self.hashList[:self.maxSizeOfHashList]
			self.updateHashSet()

	def getList(self):
		return self.hashList


def test():
	myHl = HashList(3)
	myHl.add(12)
	myHl.add(12)
	l = myHl.getList()
	print l
	myHl.add(13)
	myHl.add(14)
	myHl.add(11)
	myHl.add(16)
	l = myHl.getList()
	print l




if __name__ == '__main__':
	test()



class HashSet:
	def __init__(self):
		self.hashSet = set()

	def size(self):
		return len(self.hashSet)

	def clear(self):
		self.hashSet.clear()

	def insert(self, value):
		self.hashSet.add(value)

	#if the value is new, then it will return true else return false
	def insertNewValue(self,value):
		oldSize = self.size()
		self.insert(value)
		newSize = self.size()
		if newSize > oldSize :
			return True
		return False

	# convert the hash set to hash list
	def toHashList(self):
		return sorted(list(self.hashSet))

	def getList(self, hashList):
		self.hashSet = set(hashList)


def test():
	myHashSet = HashSet()
	myHashSet.insert(12)
	myHashSet.insert(13)
	print myHashSet.insert(13)
	myHashSet.insert(10)
	print myHashSet.toHashList()

if __name__ == '__main__':
	test()

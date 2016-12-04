
import Queue as Q

class MinHashHeap:
	def __init__(self):
		self.hash = Q.PriorityQueue()

	def put(self, value):
		self.hash.put(value)

	def pop(self):
		return self.hash.get()

	def top(self):
		item = self.pop()
		self.put(item)
		return item

	def getTopRange(self, topRange):
		result = []
		for i in range(topRange):
			result += self.pop()
		return result
	# clear
	# empty
	# size

# test 
def test():
	my = MinHashHeap()
	my.put(10)
	my.put(20)
	my.put(15)
	print my.pop()
	my.put(5)
	print my.pop()



if __name__ == '__main__':
	test()
import sys
from murmurhash import *
from MinHashHeap import *

from HashList import *

class Sketch:

	# init sketch
	def __init__(self, kmerSize = 10, maxSizeOfHashList = 10):
		self.kmerSize = kmerSize

		self.hashList = HashList(maxSizeOfHashList)

		self.hashes = []
		self.maxHashSize = 10
		self.maxHashValue = 0
	

	def addToHashes(self,value):
		self.hashList.add(value)




	def getHashesFromFile(self, filename):
		input_file = open(filename,'r')
		
		seq = ''
		for ln in input_file:
			if ln[0] == '>':
				continue
			seq += ln.strip()

		for i in xrange(len(seq) - self.kmerSize + 1):
			kmer = seq[i:i+self.kmerSize]
			self.addToHashes(murmur64(kmer))




# for test 
def test():
	mySketch = Sketch()
	filename = 'genome1.fna'
	mySketch.getHashesFromFile(filename)
	print mySketch.hashList.getList()
	

if __name__ == '__main__':
	test()
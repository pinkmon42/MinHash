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

		if len(self.hashes) < self.maxHashSize:
			self.hashes.append(value)
			if value > self.maxHashValue:
				self.maxHashValue = value
		else :
			if value < self.maxHashValue:
				self.hashes.append(value)
				self.hashes = sorted(self.hashes)[:self.maxHashSize]




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


	def getMinHash(self, minHashSize):
		for i in range(minHashSize):




# for test 
def test():
	mySketch = Sketch()
	filename = 'genome1.fna'
	mySketch.getHashesFromFile(filename)
	print mySketch.hashes
	

if __name__ == '__main__':
	test()
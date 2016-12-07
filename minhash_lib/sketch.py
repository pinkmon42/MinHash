import sys
from murmurhash import *
from MinHashHeap import *
from HashList import *

class Sketch:

	# init sketch
	def __init__(self, kmerSize = 21, maxSizeOfHashList = 1000):
		self.kmerSize = kmerSize
		self.hashList = HashList(maxSizeOfHashList)
	
	def addToHashes(self,value):
		self.hashList.add(value)

	def buildSketch(self, input_filename, output_filename):
		self.getHashesFromFile(input_filename)
		self.writeSketch(output_filename)

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

	def writeSketch(self,filename):
		output_file = open(filename,'w')
		hl = self.hashList.getList()
		for i in hl:
			s = str(i) + '\n'
			output_file.write(s)
		output_file.close()

# for test 
def test():
	mySketch1 = Sketch()

	mySketch1.buildSketch('genome1.fna', 'genome1.msh')



if __name__ == '__main__':
	test()
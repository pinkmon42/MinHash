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

<<<<<<< HEAD

	def buildSketch(self, input_filename, output_filename):
		self.getHashesFromFile(input_filename)
		self.writeSketch(output_filename)

=======
>>>>>>> 8cec258861daa8efa60bd2aef96e8b0f83de2d71
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
<<<<<<< HEAD
	mySketch1.buildSketch('genome1.fna', 'genome1.msh')
=======
	filename = 'genome1.fna'
	mySketch1.getHashesFromFile(filename)
	mySketch1.writeSketch('genome1.msh')

	mySketch2 = Sketch()
	filename = 'genome2.fna'
	mySketch2.getHashesFromFile(filename)
	mySketch2.writeSketch('genome2.msh')
>>>>>>> 8cec258861daa8efa60bd2aef96e8b0f83de2d71


if __name__ == '__main__':
	test()
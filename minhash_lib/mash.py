'''
A simple implementation of mash
bottom sketch minhash
'''

import mmh3
import itertools
import util

max_prime = 1610612741

class Mash:
	def __init__(self, kmer_size = 21, sketch_size = 10, filename = 'test.fna'):

		if filename == None:
			raise

		self.kmer_size = kmer_size
		self.sketch_size = sketch_size
		self.filename = filename

		self.sketch = [max_prime] * sketch_size

		self.prime = max_prime


	def get_sketch(self):
		seq = get_seq(self.filename)
		for kmer in yield_kmers(seq, self.kmer_size):
			
			r = mmh3.hash(kmer)
			
			if r > self.sketch[self.sketch_size - 1]:
				continue
			
			if r in self.sketch:
				continue
			
			for index, item in enumerate(self.sketch):
				if r < item:
					self.sketch.insert(index, r)
					break
			if len(self.sketch) > self.sketch_size:
				self.sketch = self.sketch[0: self.sketch_size]

def get_seq(filename):
	seq = ''
	with open(filename,'r') as file:
		for line in file:
			if line[0] == '>':
				continue
			seq += line.strip()
	return seq

def yield_kmers(seq, kmer_size):
	for i in range(len(seq) - kmer_size + 1):
		yield seq[i: i+kmer_size]

def test():
	myMash = Mash()
	myMash.get_sketch()
	print myMash.sketch

if __name__ == '__main__':
	test()



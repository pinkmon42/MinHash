'''
A simple implementation of mash
bottom sketch minhash
'''

import mmh3
import itertools
import util

max_prime = 1610612741

class Mash:
	def __init__(self, kmer_size = 21, sketch_size = 10, filename = None):

		if filename == None:
			raise Exception

		self.kmer_size = kmer_size
		self.sketch_size = sketch_size
		self.filename = filename

		# sketch size << number of total kmers
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
					self.sketch.pop()
					break
		self.get_true_sketch()

	def get_true_sketch(self):
		true_sketch = []

		for item in self.sketch:
			if item == max_prime:
				continue
			true_sketch.append(item)

		self.sketch = true_sketch
		self.sketch_size = len(true_sketch)

	def common(self, other):
		com = 0
		for item in self.sketch:
			if item in other.sketch:
				com += 1
		return com

	def jaccard(self, other):
		return self.common(other) * 1.0 / (other.sketch_size + self.sketch_size)


def get_seq(filename):
	seq = ''
	with open(filename,'r') as file:
		for line in file:
			if line[0] == '>':
				continue
			seq += line.strip()
	seq.replace('N', 'G')
	return seq

def yield_kmers(seq, kmer_size):
	for i in range(len(seq) - kmer_size + 1):
		yield seq[i: i+kmer_size]

def test():
	myMash = Mash(filename = 'test.fna')
	myMash.get_sketch()
	print myMash.sketch
	m2 = Mash(filename = 'test2.fna')
	m2.get_sketch()
	print m2.sketch

	print myMash.common(m2)
	print myMash.jaccard(m2)


if __name__ == '__main__':
	test()



'''
A simple implementation of mash
bottom sketch minhash
'''

import mmh3
import itertools
import util

max_prime = 1610612741

class Mash:
	def __init__(self, kmer_size = 15, sketch_size = 1000, filename = None):

		if filename == None:
			raise Exception

		self.kmer_size = kmer_size
		self.sketch_size = sketch_size
		self.filename = filename

		self.name = filename.split('.')[0]

		# sketch size << number of total kmers
		self.sketch = [max_prime] * sketch_size

		self.prime = max_prime

		self.get_sketch()


	def get_sketch(self):
		seq = get_seq(self.filename)
		for kmer in yield_kmers(seq, self.kmer_size):
			
			r = mmh3.hash(kmer) % max_prime
			
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



# example mash

import os

# all data in /lash/data directory
def get_file_path(filename):
	script_dir = os.path.dirname(__file__)
	s = script_dir.split('/')
	path = '/'.join(s[:-1])
	path += '/data/' + filename
	return path

def get_pair_result():

	for i in range(10):
		seq1 = 'sequence' + str(i) + '.fasta.txt'
		path1 = get_file_path(seq1)
		m1 = Mash(filename = path1)
		
		for j in range(10):
			if i == j :
				continue
			seq2 = 'sequence' + str(j) + '.fasta.txt'
			path2 = get_file_path(seq2)
			m2 = Mash(filename = path2)

			print seq1,'jaccard distance to',seq2, m1.jaccard(m2)

if __name__ == '__main__':
	get_pair_result()











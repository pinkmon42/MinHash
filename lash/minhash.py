import util
import pickle
import numpy as np
import mmh3
import os

max_prime = 1610612741

class MinHash:
	'''
		MinHash
	'''

	def __init__(self, filename = None, kmer_size = 100, signature_size = 100):
		# the max size of signature can not be bigger than 1000
		if filename == None or kmer_size == None:
			raise
		if signature_size == None:
			raise
		self.filename = filename
		self.name = filename.split('.')[0]

		self.kmer_size = kmer_size

		#self.kmers = util.get_kmers(filename,kmer_size)
		self.signature_size = signature_size
		self.hashtable = util.get_hashtable(signature_size)
		#self.signature = self.get_signature()
		self.get_signature_xor()
	
	def get_signature_xor(self):
		'''
		generate signatures using xor hash
		'''
		seq = util.get_seq(self.filename)
		xortable = get_xor_hashtable(self.signature_size)

		sig = [max_prime] * self.signature_size

		print 'start'
		for kmer in util.yield_kmers(seq, self.kmer_size):
			r = mmh3.hash(kmer)
			for i in range(self.signature_size):
				sig[i] = min(sig[i], r^xortable[i] % max_prime)
				

		self.signature = sig

	def get_signature_simple(self):
		'''
		get signature simple hash version
		'''
		sig = []
		for coeff in self.hashtable:
			min_sig = max_prime
			a,b = coeff[0], coeff[1]
			for kmer in self.kmers:
				r = (a * kmer + b) % max_prime
				if r < min_sig:
					min_sig = r
			sig.append(r)
		return sig

	def rotate_hash(self):
		'''
		get signature rotate hash version
		'''
		
		pass

	def write_sig_file(self):
		output_file = ''.join((self.name, '.sig'))
		with open(output_file, 'w') as f:
			for sig in self.signature:
				f.write(str(sig)+"\n")
	
	def common(self, other):
		com = 0
		for item in self.signature:
			if item in other.signature:
				com += 1
		return com

	def jaccard(self, other):
		return self.common(other) * 1.0 / (self.signature_size + other.signature_size)


def set_xor_hash():
	if os.path.isfile('xorhash.txt'):
		return

	xortable = np.random.randint(0, max_prime, 1000)
	with open('xorhash.txt','w') as fp:
		pickle.dump(xortable, fp)

def get_xor_hashtable(size):
	if not os.path.isfile('xorhash.txt'):
		set_xor_hash()

	table = []
	with open('xorhash.txt','r') as fp:
		table = pickle.load(fp)

	return table[:size]


def test_minHash():
	a = MinHash('genome2.fna',21,128)
	b = MinHash('genome3.fna',21,128)

	set_xor_hash()
	print get_xor_hashtable(10)
	a.get_signature_xor()
	print a.signature
	b.get_signature_xor()

# example minhash

import os

# all data in /lash/data directory
def get_file_path(filename):
	script_dir = os.path.dirname(__file__)
	s = script_dir.split('/')
	path = '/'.join(s[:-1])
	path += '/data/' + filename
	return path

def get_pair_result():
	set_xor_hash()
	for i in range(10):
		seq1 = 'sequence' + str(i) + '.fasta.txt'
		path1 = get_file_path(seq1)
		m1 = MinHash(filename = path1)
		
		for j in range(10):
			if i == j :
				continue
			seq2 = 'sequence' + str(j) + '.fasta.txt'
			path2 = get_file_path(seq2)
			m2 = MinHash(filename = path2)

			print seq1,'jaccard distance to',seq2, m1.jaccard(m2)

if __name__ == '__main__':
	get_pair_result()











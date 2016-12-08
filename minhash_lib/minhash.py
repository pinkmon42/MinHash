import util
import pickle
import numpy as np
import mmh3


max_prime = 1610612741

class MinHash:
	'''
		MinHash
	'''

	def __init__(self, filename = None, kmer_size = None, signature_size = None):
		# the max size of signature can not be bigger than 1000
		if filename == None or kmer_size == None:
			raise
		if signature_size == None:
			raise
		self.filename = filename
		self.kmer_size = kmer_size

		self.kmers = util.get_kmers(filename,kmer_size)
		self.signature_size = signature_size
		self.hashtable = util.get_hashtable(signature_size)
		self.signature = self.get_signature()


	def get_signature(self):
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
		output_file = ''.join((self.filename, '.sig'))
		with open(output_file, 'w') as f:
			for sig in self.signature:
				f.write(str(sig)+"\n")
	
	
	def get_signature_xor(self):
		'''
		generate signatures using xor hash
		'''
		seq = util.get_seq(self.filename)
		xortable = get_xor_hashtable(self.signature_size)

		sig = [max_prime] * self.signature_size

		for kmer in util.yield_kmers(seq, self.kmer_size):
			r = mmh3.hash(kmer)
			for i in range(self.signature_size):
				sig[i] = min(sig[i], r^xortable[i] % max_prime)

		self.signature = sig

	def common(self, other):
		com = 0
		for item in self.signature:
			if item in other.signature:
				com += 1
		return com

	def jaccard(self, other):
		return self.common(other) * 1.0 / (self.signature_size + other.signature_size)





def set_xor_hash():
	xortable = np.random.randint(0, max_prime, 1000)
	with open('xorhash.txt','w') as fp:
		pickle.dump(xortable, fp)

def get_xor_hashtable(size):
	table = []
	with open('xorhash.txt','r') as fp:
		table = pickle.load(fp)

	return table[:size]


def test_minHash():
	a = MinHash('test.fna',21,128)
	b = MinHash('test2.fna',21,128)
	a.write_sig_file()
	b.write_sig_file()

	set_xor_hash()
	print get_xor_hashtable(10)
	a.get_signature_xor()
	print a.signature
	b.get_signature_xor()

	print a.common(b)
	print a.jaccard(b)

if __name__ == '__main__':
	test_minHash()

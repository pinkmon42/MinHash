import util
import pickle


class MinHash:
	'''
		MinHash
	'''

	def __init__(self, readfile = None, kmersize = None, signature_size = None):
		if readfile == None or kmersize == None:
			raise
		if signature_size == None:
			raise
		self.filename = readfile.split('.')[0]
		self.kmers = util.get_kmers(readfile,kmersize)
		self.signature_size = signature_size
		self.hashtable = util.get_hashtable(signature_size)
		self.signature = self.get_signature()


	def get_signature(self):
		'''
		get signature simple hash version
		'''
		sig = []
		for coeff in self.hashtable:
			min_sig = 4294967311
			a,b = coeff[0], coeff[1]
			for kmer in self.kmers:
				r = (a * kmer + b) % 4294967311
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
	

def test_minHash():
	a = MinHash('test.fna',21,128)
	b = MinHash('test2.fna',21,128)
	a.write_sig_file()
	b.write_sig_file()

if __name__ == '__main__':
	test_minHash()

import util

class LSH():
	def __init__(self, kmer_size, sig_size, band_num):

		self.kmer_size = kmer_size
		self.sig_size = sig_size
		self.band_num = band_num
		self.band_size = sig_size / band_num

		self.seq_dic = {} # dictionary of sequence
		
		self.seq_num = 0

		self.sig = []
		self.bands = []


	def add(self, filename):
		'''
		add new sequences to LSH
		'''

		index = self.seq_num
		self.seq_num = index + 1

		kmers = util.get_kmers(filename, self.kmer_size)

		# need to change the hash function to different hash function
		l = []
		# need to change the hash part
		for i in range(self.sig_size):
			l.append(min(map(hash, kmers)))
		self.sig.append([])
		self.sig[index] = l

		b = []
		for i in range(self.band_num):
			b.append(self.get_band_value(l[i:i+self.band_size]))
		self.bands.append([])
		self.bands[index] = b


	def update(self):
		'''
		update signature matrix after adding new sequences
		then update bands matrix 
		'''
		pass 

	def get_signature(self, seq):
		'''
		do hash to the sequence, in this case, k-mers
		use the smallest value for every hash
		'''
		pass

	def get_band_value(self, vector):
		'''
		hash the vector to bucket
		'''

		# need to change the hash part
		s = 0
		for i in vector:
			s += i

		return s % 17

	def get_pairs(self, seq_index):
		'''
		get the pairs more common in the same bucket
		'''
		pair = []
		for i in range(self.band_num):
		
			seq_bucket = column(self.bands,seq_index)
			print seq_bucket
			pair.append([])
			for index, value in enumerate(seq_bucket):
				if value == seq_bucket[seq_index] and not index == seq_index:
					pair[i].append(index)

		print pair


	def query(self, new_sequence):
		'''
		directly query that the bucket that the new sequence is in
		'''
		pass

def column(matrix, i):
	return [row[i] for row in matrix]


def test():
	myLSH = LSH(20,12,3)
	myLSH.add('test.fna')
	print myLSH.sig
	print myLSH.bands
	myLSH.add('test2.fna')
	print myLSH.sig
	print myLSH.bands

	myLSH.get_pairs(0)


if __name__ == '__main__':
	test()





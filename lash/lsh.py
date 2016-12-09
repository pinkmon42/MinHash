import util
import mmh3
import minhash

max_prime = 1610612741

class LSH():
	def __init__(self, kmer_size, sig_size, band_num):

		self.kmer_size = kmer_size
		self.sig_size = sig_size
		self.band_num = band_num
		self.band_size = sig_size / band_num
		
		self.seq_num = 0

		self.instance = []

		self.sig = []
		self.bands = []

		# thredhold to count a pair as a common pair
		self.common_t = 1


	def add(self, filename):
		'''
		add new minhash instance to LSH
		'''

		index = self.seq_num
		
		self.seq_num = index + 1

		new_instance = minhash.MinHash(filename,self.kmer_size, self.sig_size)

		self.instance.append(new_instance.name)

		new_instance.get_signature_xor()

		self.sig.append([])
		self.sig[index] = new_instance.signature

		b = []
		for i in range(self.band_num):
			b.append(self.get_band_value(self.sig[index][i:i+self.band_size]))
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
		s = sum(vector)
		s = ((s >> 16) ^ s) * 0x45d9f3b
		s = ((s >> 16) ^ s) * 0x45d9f3b
		s = (s >> 16) ^ s
		return s % 4

	def get_pairs(self, seq_index):
		'''
		get the pairs more common in the same bucket
		'''
		pair = []
		for i in range(self.band_num):
			seq_bucket = column(self.bands,i)
			pair.append([])
			for index, value in enumerate(seq_bucket):
				if value == seq_bucket[seq_index] and not index == seq_index:
					pair[i].append(index)
		return pair

	def count_common(self, seq_index):
		pair = self.get_pairs(seq_index)

		count = [0] * len(self.instance)
		
		for row in pair:
			for seq_index in row:
				count[seq_index] += 1

		result = []

		for index, val in enumerate(count):
			if val >= self.common_t:
				result.append(self.instance[index])

		return result



	def query(self, new_sequence):
		'''
		directly query that the bucket that the new sequence is in
		'''
		pass

def column(matrix, i):
	return [row[i] for row in matrix]


def test():
	myLSH = LSH(42,1000,50)
	myLSH.add('genome3.fna')
	myLSH.add('genome2.fna')

	print myLSH.count_common(0)


if __name__ == '__main__':
	test()





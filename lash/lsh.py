import util
import mmh3
import minhash
import mash

max_prime = 1610612741

class LSH():
	def __init__(self, kmer_size, sig_size, band_num, band_range):

		self.kmer_size = kmer_size
		self.sig_size = sig_size
		self.band_num = band_num
		self.band_size = sig_size / band_num
		
		self.seq_num = 0

		self.instance = []

		self.sig = []
		self.bands = []

		self.band_range = band_range

		# thredhold to count a pair as a common pair
		self.common_t = 1


	def add_mash(self, filename):
		'''
		add new mash instance to LSH, signature is sketch
		'''

		index = self.seq_num
		
		self.seq_num = index + 1

		new_instance = mash.Mash(kmer_size = self.kmer_size, sketch_size = self.sig_size, filename = filename)
		
		self.instance.append(new_instance.name)

		#new_instance.get_signature_xor()

		self.sig.append([])
		self.sig[index] = new_instance.sketch

		b = []
		for i in range(self.band_num):
			b.append(self.get_band_value(self.sig[index][i:i+self.band_size]))
		self.bands.append([])
		self.bands[index] = b


	def add_minhash(self, filename):
		'''
		add new minhash instance to LSH
		'''

		index = self.seq_num
		
		self.seq_num = index + 1

		new_instance = minhash.MinHash(filename,self.kmer_size, self.sig_size)

		self.instance.append(new_instance.name)

		#new_instance.get_signature_xor()

		self.sig.append([])
		self.sig[index] = new_instance.signature

		b = []
		for i in range(self.band_num):
			b.append(self.get_band_value(self.sig[index][i:i+self.band_size]))
		self.bands.append([])
		self.bands[index] = b


	def get_band_value(self, vector):
		'''
		hash the vector to bucket
		'''
		s = sum(vector)
		s = ((s >> 16) ^ s) * 0x45d9f3b
		s = ((s >> 16) ^ s) * 0x45d9f3b
		s = (s >> 16) ^ s
		return s % self.band_range

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


def column(matrix, i):
	return [row[i] for row in matrix]


# example lsh

import os

# all data in /lash/data directory
def get_file_path(filename):
	script_dir = os.path.dirname(__file__)
	s = script_dir.split('/')
	path = '/'.join(s[:-1])
	path += '/data/' + filename
	return path

def test():
	myLSH = LSH(42, 1000, 20, 53)
	for i in range(10):
		seq1 = 'sequence' + str(i) + '.fasta.txt'
		path1 = get_file_path(seq1)
		myLSH.add_mash(filename = path1)

	print myLSH.count_common(1)


if __name__ == '__main__':
	test()





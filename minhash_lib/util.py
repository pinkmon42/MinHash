import os
import pickle
import random
from hashlib import sha1


# pickle a hash table for minHash
def save_hashtable(max_num, tablesize = 256):
	hashtable = []
	for i in range(tablesize):
		a, b = random.randint(0, max_num), random.randint(0, max_num)
		hashtable.append((a,b))

	with open('hashtable.txt','w') as ht:    
		    pickle.dump(hashtable, ht)

def get_hashtable(size):
	co_a, co_b = [] * size, [] * size
	with open('hashtable.txt','r') as ht:
		table = pickle.load(ht)
	table = table[0:size]
	return table

# to get kmers from sequence read
def get_kmers(filename, kmersize):
	'''
	get kmers from input file
	'''
	seq = ''

	with open(filename, 'r') as f:
		for ln in f:
			if ln[0] == '>':
				continue
			seq += ln.strip()

	kmers = []

	for kmer in yield_kmers(seq, kmersize):
		kmers.append(hash(kmer))

	return kmers

def yield_kmers(seq, kmersize):
	for i in range(len(seq) - kmersize + 1):
		yield ''.join(seq[i:i+kmersize])


def test():
	#print get_kmers('test.fna', 10)
	if not os.path.isfile('hashtable.txt'):
		save_hashtable(100)
	print get_hashtable(100)
	

if __name__ == '__main__':
	test()



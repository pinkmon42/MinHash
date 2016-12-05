"""
Simple minhash according to part of sourmash
can minhash sequence and return jaccard similarity
"""

import itertools

class Estimator(object):
	def __init__(self, sketchsize = 10, kmersize = 10, max_prime = 1e10):

		self.kmersize = kmersize
		self.p = get_prime(max_prime)
		self.sketch = [self.p] * sketchsize

	def get_sketch(self, seq):
		for kmer in yield_kmers(seq, self.kmersize):
			self.add(kmer)

	def add(self, kmer):
		sketch = self.sketch
		# use murmur hash to replace
		h = hash(kmer)
		h = h % self.p

		if h >= sketch[-1]:
			return

		for i,v in enumerate(sketch):
			if h < v:
				sketch.insert(i, h)
				sketch.pop()
				return
			elif h == v:
				return

	def common(self, other):
		if self.kmersize != other.kmersize:
			raise
		if self.p != other.p:
			raise

		common = 0 
		for val in yield_overlaps(self.sketch, other.sketch):
			common += 1
		return common


	def jaccard(self, other):
		hashlen = len(self.sketch)
		while hashlen and self.sketch[hashlen - 1] == self.p:
			hashlen -= 1
		if hashlen == 0:
			raise

		return self.common(other) / float(hashlen)
# generate kmers in the seq
def yield_kmers(seq, kmersize):
	for i in range(len(seq) - kmersize + 1):
		yield seq[i:i+kmersize]

#naive way to find the overlap
def yield_overlaps(x1,x2):
	i,j = 0, 0
	try:
		while 1:
			while x1[i] < x2[j]:
				i += 1
			while x1[i] > x2[j]:
				j += 1
			if x1[i] == x2[j]:
				yield x1[i]
				i += 1
				j += 1
	except IndexError:
		return

# get prime smaller than num
def get_prime(num):
	if num == 1:
		return 1

	p = int(num)

	if p %2 == 0:
		p -= 1
	while p > 0:
		if is_prime(p):
			return p
		p -= 2

# taken from khmer 2.0; original author Jason Pell.
def is_prime(number):
    """Check if a number is prime."""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for _ in range(3, int(number ** 0.5) + 1, 2):
        if number % _ == 0:
            return False
    return True

def test_Estimator():
	a = Estimator(2,3)
	b = Estimator(2,3)
	a.sketch = [1,2,3]
	b.sketch = [2,3,4]
	print a.common(b)
	print a.jaccard(b)

def test_sequence():
	a = Estimator(2,3)
	b = Estimator(2,3)
	a.get_sketch("abababab")
	b.get_sketch("ababababcdcdcdcd")
	print a.common(b)
	print a.jaccard(b)


if __name__ == '__main__':
	test_Estimator()
	test_sequence()


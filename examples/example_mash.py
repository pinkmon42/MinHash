import os
from lash.util import *
from lash.mash import * 

# all data in /lash/data directory
def get_file_path(filename):
	script_dir = os.path.dirname(__file__)
	s = script_dir.split('/')
	path = '/'.join(s[:-1])
	path += '/data/' + filename
	return path

path = get_file_path('sequence0.fasta.txt')
m1 = Mash(filename = path)
m1.get_sketch()
print m1.sketch

path = get_file_path('sequence1.fasta.txt')
m2 = Mash(filename = path)
m2.get_sketch()

path = get_file_path('sequence2.fasta.txt')
m3 = Mash(filename = path)
m3.get_sketch()

print m1.jaccard(m2)
print m1.jaccard(m3)








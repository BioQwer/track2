#!/usr/bin/python -u
import sys, os, pickle
from collections import defaultdict
from multiprocessing import Pool,cpu_count
from time import time
from is_abbr import *


def select_valid_pair(a):
	global filtered_name_set
	# TODO: This is *at least* O(N^2) with 85K names == 7 billion calls to is_abbr
	# since we only care about prefix matches, we could use a prefix (or 1st letter) index
	# instead of doing an exhaustive search
	return [(a, e) for e in filtered_name_set if is_abbr(a, e)]

def main():
	if len(sys.argv) != 4:
		sys.stderr.write('Usage: %s filtered_name_set_pickle output_path output_suffix\n' % (sys.argv[0]))
		exit(1)
	
	global filtered_name_set
	with open(sys.argv[1], 'rb') as f:
		filtered_name_set = pickle.load(f)

	if '' in filtered_name_set:
		filtered_name_set.remove('')
	abbr_dict = defaultdict(set)
	extend_dict = defaultdict(set)

	count = 0
	p = Pool(cpu_count()-1) # leave one core for overhead
	print '#filtered_name = ',len(filtered_name_set)
	start = time()
	
	# FIXME: The next line takes 6+ hrs on 3 cores! O(N^2)
	abbr_extend_pair_sets = p.map(select_valid_pair, filtered_name_set)
	
	print '# of abbr_extend_pair_sets= ',len(abbr_extend_pair_sets)
	for pair_set in abbr_extend_pair_sets:
		for pair in pair_set:
			abbr_dict[pair[1]].add(pair[0])
			extend_dict[pair[0]].add(pair[1])
			count += 1
	p.close()
	p.join()

	print (time() - start) / len(filtered_name_set), 'seconds' # 0.27 sec * 85632 = 2312 or 6+ hrs
	print 'count = ', count
	with open(os.path.join(sys.argv[2], 'abbr_dict_' + sys.argv[3] + '.pkl'), 'wb') as f:
		pickle.dump(abbr_dict, f)
	with open(os.path.join(sys.argv[2], 'extend_dict_' + sys.argv[3] + '.pkl'), 'wb') as f:
		pickle.dump(extend_dict, f)
	
if __name__ == "__main__":
	main()


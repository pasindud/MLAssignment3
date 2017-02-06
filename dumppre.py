import itertools
import sys
import random
features = [1, 2, 3,4,5,6,7,8,9,10,
			11,12,13,14,15,16,17,18,19,20,
			21,22,23,24,25,26,27,28,29,30,
			31,32,33,34,35,36,37,38,39,40,
			41,42,43,44,45,46,47,48,49,50,
			51,52,53,54,55,56,57];

def random_combinations(matrix, size):
    seen = set()
    n = len(matrix)
    while True:
        new_sample = tuple(sorted(random.sample(xrange(n), size)))
        if new_sample not in seen:
            seen.add(new_sample)
            yield tuple(matrix[i] for i in new_sample)

def main(argv):
	perms = itertools.permutations(features)

	for j in xrange(1, len(features) + 1):
		k = 0
		# b = [ features[i] for i in sorted(random.sample(xrange(len(features)), j)) ]
		# b = [x[1] for x in sorted(random.sample(enumerate(features),j))]
		# indices = random.sample(range(len(myList)), K)
		b = list(itertools.islice(random_combinations(features, j), 10))
		permsstr = ""
		print j
		for p in b:
			permsstr += ','.join(str(e) for e in p) + "\n"
			writea(permsstr)

		# b = sorted(random.sample(features, i))
		# print j, "\n", b

		# comb = itertools.combinations(features, i)
		# permsstr = ""
		# for p in comb:
		# 	permsstr += ','.join(str(e) for e in p) + "\n"
		# 	k += 1
		# 	print i, k
		# 	if k > 500:
		# 		break;
		# writea(permsstr)

	# for p in perms:
	# 	permsstr += ','.join(str(e) for e in p) + "\n"
	# 	i +=1
	# 	if i == 500:
	# 		break
def writea(permsstr):
	f = open("/Users/Pasindu/Downloads/ML_Assignment/perms10.txt", 'ab')
	f.write(permsstr)
	f.close()


if __name__ == "__main__":
	main(sys.argv)
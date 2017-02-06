from multiprocessing import Pool
import oct2py
import sys
from multiprocessing import Process
from multiprocessing import Queue
import matplotlib.pyplot as plt
import pprint

"""

export OCTAVE_EXECUTABLE=/usr/local/octave/3.8.0/bin/octave-3.8.0

"""

lambdanum = 1.0
features = [1, 2, 3,4,5,6,7,8,9,10,
			11,12,13,14,15,16,17,18,19,20,
			21,22,23,24,25,26,27,28,29,30,
			31,32,33,34,35,36,37,38,39,40,
			41,42,43,44,45,46,47,48,49,50,
			51,52,53,54,55,56,57];
MLPATH="/Users/Pasindu/Downloads/ML_Assignment/mltool-master/classifiers"
FEATURE_COMBINATION_FILE = "perms10.txt"
PATH_TO_RESULTS_FILE = "/Users/Pasindu/Downloads/ML_Assignment/results1.txt"

def parrlle_spam_one(feature_set_no, features, method, lamba):
	oc = oct2py.Oct2Py()
	oc.addpath(MLPATH)
	[accuracy, sensitivity] = oc.run_spam_algo(method, lamba, features)
	write_result(feature_set_no, features, method, lamba, accuracy, sensitivity)

def write_result(feature_set_no, features, method, lamba, accuracy, sensitivity):
	args = [feature_set_no, features, method, lamba, accuracy, sensitivity]
	args = [str(e) for e in args]
	print args
	f = open(PATH_TO_RESULTS_FILE, 'ab')
	f.write("\t\n".join(args))
	f.close()

def parrlle_spam():
	i = 0
	for x in open(FEATURE_COMBINATION_FILE):
		feats = []
		feats.append([int(e) for e in x.split(",")])
		method = "logistic"
		print feats[0]
		p = Process(target=parrlle_spam_one, args=(i, feats[0], method, lambdanum))
		p.start()
		p.join()
		i +=1

def main(argv):
	parrlle_spam()
	exit(0)

	# Comment above to run test
	oc = oct2py.Oct2Py()
	oc.addpath(MLPATH)
	method = "logistic"
	
	# Test wether coloums or rows
	[accuracy, sensitivity, feats] = oc.run_spam_algo(method, lambdanum, [1,3])
	print accuracy,sensitivity, feats

	[accuracy, sensitivity, feats] = oc.run_spam_algo(method, lambdanum, [[1,3]])
	print accuracy,sensitivity, feats

if __name__ == "__main__":
	main(sys.argv)
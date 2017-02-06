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

def parrlle_spam_one(features, method, lamba):
	oc = oct2py.Oct2Py()
	oc.addpath("/Users/Pasindu/Downloads/p2")
	[accuracy, sensitivity] = oc.run_spam_algo(method, lamba, features)
	print accuracy
	print sensitivity


def parrlle_spam():
	for x in open("perms10.txt"):
		feats = []
		feats.append([int(e) for e in x.split(",")])
		method = "logistic"
		print feats[0]
		p = Process(target=parrlle_spam_one, args=(feats[0], method, lambdanum))
		p.start()
		p.join()

def main(argv):
	parrlle_spam()
	exit(0)
	oc = oct2py.Oct2Py()
	oc.addpath("/Users/Pasindu/Downloads/p2")
	method = "logistic"
	[accuracy, sensitivity] = oc.run_spam_algo(method, lambdanum, features)
	print accuracy
	print sensitivity
	

if __name__ == "__main__":
	main(sys.argv)
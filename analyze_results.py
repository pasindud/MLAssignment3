
import sys
import ast
import operator
FILENAME = "example_feature_results.txt"
FILENAME = "results_ubuntu_12_all_methods.txt"
FILENAME = "results_ubuntu_12_all_methods.txt"
FILENAME2 = "results_ubuntu_11_all_methods_final_1.txt" 
FILENAME = "final_all_results.txt" 

features = [1, 2, 3,4,5,6,7,8,9,10,
                        11,12,13,14,15,16,17,18,19,20,
                        21,22,23,24,25,26,27,28,29,30,
                        31,32,33,34,35,36,37,38,39,40,
                        41,42,43,44,45,46,47,48,49,50,
                        51,52,53,54,55,56,57];


def writer(fname, c):
	f = open(fname, "w")
	f.write(c)
	f.close()


def main(argv):
	data_svm = []
	data_logistic = []
	data_rigde = []
	a_set = set()
	for line in open(FILENAME):
		# try:
			line = line.rstrip()
			segs = line.split("\t")

			features = ast.literal_eval(segs[1])
			algo = segs[2].strip()
			lamda = segs[3]
			a_set.add(lamda)
			accuracy = segs[4]
			sensitivity = segs[5]
			classibias = ast.literal_eval(segs[6].rstrip())

			weights = segs[7].rstrip().replace("[", "").replace("]", "")
			weights = "[" + ",".join(filter(None, weights.split(" "))) + "]"
			weights = ast.literal_eval(weights)
			# print weights

			d = {"features" : features, 
				"lamda" : lamda, 
				"accuracy" : float(accuracy),
				"sensitivity" : float(sensitivity),
				"weights": weights, 
				"classibias": float(classibias)}

			if algo == "svm":
				data_svm.append(d)
			elif(algo == "ridge") :
				data_rigde.append(d)
			elif(algo == "logistic"):
				data_logistic.append(d)
			else:
				print "nothing for ", d

	writer("ridge_scores.txt", score_features(data_rigde))
	writer("logistic_scores.txt", score_features(data_logistic))
	writer("svm_scores.txt", score_features(data_svm))

	# print a_set

def score_features(results):
	features_scores = {}
	features_occurence = []

	# Null zero features
	features_occurence.append(0)

	for f in features:
		features_scores[str(f)] =  0
		features_occurence.append(0)

	for point in results:
		gobal_score = get_score(point['accuracy'], point['sensitivity'], point['classibias'])

		index = 0
		for f in point['features']:
			weight = point['weights'][index]
			score_now = features_scores[str(f)]
			features_scores[str(f)] = score_now + weight + gobal_score
			features_occurence[f] = features_occurence[f] + 1
			index += 1

	#  Averaging the scores according to the occrurance.
	for f in features:
		score_now = features_scores[str(f)]
		features_scores[str(f)] = score_now / features_occurence[f]

	s1 = sorted(features_scores.items(), key=operator.itemgetter(0))
	sorted_scores = sorted(s1, key=operator.itemgetter(1), reverse=True)

	output = ""
	for k in sorted_scores:
		print k
		output += "feature - %s score - %s \n" %(k[0], k[1])
	return output 


def get_score(a,s, wo):
	return a + s+ wo;

if __name__ == "__main__":
	main(sys.argv)

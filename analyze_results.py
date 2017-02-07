
import sys
import ast

FILENAME = "example_feature_results.txt"
FILENAME = "results_ubuntu_11_all_methods.txt"

def main(argv):
	data_svm = []
	data_logistic = []
	data_rigde = []

	for line in open(FILENAME):
		# try:
			line = line.rstrip()
			segs = line.split("\t")

			features = ast.literal_eval(segs[1])
			algo = segs[2]
			lamda = segs[3]
			accuracy = segs[4]
			sensitivity = segs[5]
			w = ast.literal_eval(segs[6].rstrip())

			classbia1 = segs[7].rstrip().replace("[", "").replace("]", "")
			classbia2 = "[" + ",".join(filter(None, classbia1.split(" "))) + "]"
			classbia3 = ast.literal_eval(classbia2)

			d = {"features" : features, 
				"lamda" : lamda, 
				"accuracy" : accuracy,
				"sensitivity" : sensitivity,
				"classibias": classbia3, 
				"w": w}

			print d
			# break
		# except ValueError as ex :
		# 	print ex
		# 	print "Error - ", line
		# 	break
		# data.append(segs)



if __name__ == "__main__":
	main(sys.argv)
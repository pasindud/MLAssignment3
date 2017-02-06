

import sys

def main(args):
	o = {}
	for line in open(args[1]):
		segs = line.split(",")
		for i in xrange(0,len(segs)):
			if not segs[i] == "0":
				o.update({i : "T"})
	for x in o:
		print x

if __name__ == "__main__":
	main(sys.argv)


import sys
import numpy as np
# from sklearn.decomposition import PCA as PCAA
from matplotlib.mlab import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score

# from sklearn.decomposition import PCA

def main(argv):
	data = []
	NUM = 0
	for line in open("spam.data"):
		seg = line.rstrip().split(",")
		a = []
		for b in seg:
			a.append(float(b))
		NUM = len(a)
		data.append(a)

	fig1 = plt.figure() # Make a plotting figure
	ax = Axes3D(fig1) # use the plotting figure to create a Axis3D object.

	X = np.array(data)
	newData  = PCA(X)
	proj = newData.project(X)
	print(newData.numcols)
	print(newData.a)

	# a = newData.fracs(:59)
	num_of_clusters = 2
	kmeans = KMeans(n_clusters=num_of_clusters)
	colrs = kmeans.fit_predict(X)
	col = np.arange(30)


	# exit(0)
	x = []
	y = []
	z = []

	k = 0
	for item in newData.Y:
		x.append(item[0])
		y.append(item[1])
		z.append(item[2])

	print len(x)
	print len(y)
	print len(z)
	for i,xi in enumerate(x):
		k =+1
		ax.scatter(x[i],y[i],z[i])

	ax.plot(newData[:, 0], newData[:, 1], '.', mfc=clr1, mec=clr1)

	plt.show()



if __name__ == "__main__":
	main(sys.argv)

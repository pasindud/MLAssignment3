
import sys
import numpy as np
# from sklearn.decomposition import PCA as PCAA
from matplotlib.mlab import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



def main(argv):
	data = []
	NUM = 0
	for line in open("/Users/Pasindu/Downloads/ML_Assignment/spam.data"):
		seg = line.rstrip().split(",")
		a = []
		for b in seg:
			a.append(float(b))
		NUM = len(a)
		data.append(a)

	fig1 = plt.figure() # Make a plotting figure
	ax = Axes3D(fig1) # use the plotting figure to create a Axis3D object.

	X = np.array(data)
	# print NUM
	# pca = PCA(n_components=NUM)
	# pca.fit(X)
	# X_new = pca.transform(X)
	# print(len(X[0]))
	# print(len(X_new[0]))
	# print (X_new)

	newData  = PCA(X)
	print(newData.numcols)
	print(newData.a)


	col = np.arange(30)

	x = []
	y = []
	z = []

	for item in newData.Y:
		x.append(item[0])
		y.append(item[1])
		z.append(item[2])

	for i,xi in enumerate(x):
		ax.scatter(x[i],y[i],z[i])
	# ax1.plot(newData[:, 0], newData[:, 1], '.', mfc=clr1, mec=clr1)
	plt.show()



if __name__ == "__main__":
	main(sys.argv)
from numpy import array
from numpy import *

def img2vector(filename):
	returnVect = zeros((1, 1024))
	fr = open(filename)
	for i in range(32):
		lineStr = fr.readline()

		for j in range(32):
			returnVect[0, 32*i+j] = int(lineStr[j])

	return returnVect


if __name__ == '__main__':
	filename = "/Users/Victor/Desktop/MachineLearningInAction/machinelearninginaction/Ch02/digits/trainingDigits/0_0.txt"

	print(img2vector(filename))
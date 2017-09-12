#!usr/bin/env python
import numpy as np

if __name__=="__main__":

	Pss = 0.8
	Pcs = 0.2
	Prs = 0.0
	Psc = 0.4
	Pcc = 0.4
	Prc = 0.2
	Psr = 0.2
	Pcr = 0.6
	Prr = 0.2

	probs=np.matrix([[Pss, Psc, Psr],[Pcs, Pcc, Pcr],[Prs, Prc, Prr]])

	# We are trying to solve P=probs*P. Hence we need eigenvector for eigenvalue of 1.

	w,v = np.linalg.eig(probs)

	standardDist = v[:,0]/np.sum(v[:,0])
	#Normalize the vector so that sum equals one for the probabilities.

	print (standardDist)
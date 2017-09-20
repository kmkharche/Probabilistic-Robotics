#!usr/bin/env python

import numpy as np

if __name__=="__main__":

	mu = np.array([0.,0.,0.])
	sigma = np.matrix([[0.01,0.,0.],[0.,0.01,0.],[0.,0.,10000.]])

	# prediction step
	mu_new = np.array([mu[0]+np.cos(mu[2]), mu[1]+np.sin(mu[2]), mu[2]])
	
	Gt = np.matrix([[1., 0., -np.sin(mu[2])],[0., 1., np.cos(mu[2])],[0., 0., 1.]])
	sigma_new = Gt*sigma*np.transpose(Gt)	# No Rt since motion is perfect

	mu = mu_new
	sigma = sigma_new

	print (mu)
	print (sigma)

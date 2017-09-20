#!usr/bin/env python

import numpy as np

if __name__=="__main__":

	mu = np.matrix([[0.],[0.],[0.]])
	sigma = np.matrix([[0.01,0.,0.],[0.,0.01,0.],[0.,0.,10000.]])

	# prediction step
	mu_new = np.matrix([[mu.item(0)+np.cos(mu.item(2))], [mu.item(1)+np.sin(mu.item(2))], [mu.item(2)]])
	
	Gt = np.matrix([[1., 0., -np.sin(mu[2])],[0., 1., np.cos(mu[2])],[0., 0., 1.]])
	sigma_new = Gt*sigma*np.transpose(Gt)	# No Rt since motion is perfect

	mu = mu_new
	sigma = sigma_new

	print (mu)
	print (sigma)

	# measurement update

	Ht = np.matrix([1., 0., 0.])
	Qt = 0.01
	zt = 1.
	Kt = sigma*np.transpose(Ht)*np.linalg.inv(Ht*sigma*np.transpose(Ht)+Qt)

	mu_new = mu + Kt*(zt - mu[0])
	sigma_new = (np.identity(3) - Kt*Ht)*sigma

	mu = mu_new
	sigma = sigma_new

	print (mu)
	print (sigma)
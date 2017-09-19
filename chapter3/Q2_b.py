#!usr/bin/env python

import numpy as np

if __name__=="__main__":

	#state vector = [x,xdot]
	prevState = np.matrix([0.0,0.0])
	currentState = np.transpose(prevState)

	totalTime = 5
	delta_time = 1.0
	mu_control = 0.0
	sigma_control = 1

	A = np.matrix([[ 1, delta_time] , [ 0, 1 ]])

	Rt = np.matrix([[(delta_time**2)/2.0,0.0] , [delta_time,0.0]])
	Sigma_t=np.matrix([[0.,0.],[0.,0.]])

	for i in range(totalTime):

		acceleration = np.random.normal(mu_control,sigma_control,1)
		currentState = A*currentState
		Sigma_t = A*Sigma_t*np.transpose(A) + Rt

		print "Time = ", i

		print "mu = ", currentState
		print "covariance = ", Sigma_t

	# measurement update
	C = np.matrix([1.0,0.0])
	Q = 10

	zt =5 
	Kt = Sigma_t*np.transpose(C)*(np.linalg.inv(C*Sigma_t*np.transpose(C) + Q))
	newState = currentState + Kt*(zt - C*currentState)
	currentState = newState

	I = np.matrix([[1.,0.],[0.,1.]])
	Sigma_t = (I - Kt*C)*Sigma_t

	print "After measurement, at time = 5"
	print "mu = ", currentState
	print "covariance = ", Sigma_t
	
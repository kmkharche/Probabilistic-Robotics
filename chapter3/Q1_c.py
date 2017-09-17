#!usr/bin/env python

import numpy as np

def predictNextState(prevState,A,R):

	state = A*prevState + R
	return state

if __name__=="__main__":

	#state vector = [x,xdot]
	prevState = np.matrix([0.0,0.0])
	currentState = np.transpose(prevState)

	totalTime = 5
	delta_time = 1.0
	mu_control = 0.0
	sigma_control = 1

	A = np.matrix([[ 1, delta_time] , [ 0, 1 ]])

	factor = np.matrix([[(delta_time**2)/2.0] , [delta_time]])

	for i in range(totalTime):

		acceleration = np.random.normal(mu_control,sigma_control,1)
		Rt = factor*acceleration
		currentState = predictNextState(currentState,A,Rt)

		print "Time = ", i
		print "Acceleration = ", acceleration

		print (currentState)
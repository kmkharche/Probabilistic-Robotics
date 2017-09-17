#!usr/bin/env python

import numpy as np

def predictNextState(prevState,control,A,B):

	state = A*prevState + B*control
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

	B = np.matrix([[(delta_time**2)/2.0] , [delta_time]])
	
	for i in range(totalTime):

		control = np.random.normal(mu_control,sigma_control,1)
		currentState = predictNextState(currentState,control,A,B)

		print "Time = ", i
		print "Acceleration = ", control

		print (currentState)
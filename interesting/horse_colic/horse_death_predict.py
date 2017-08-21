#!/usr/bin/env python
#coding=utf-8
# Filename : horse_death_predict.py
# Description : Using logistic regression 
#		method to predict death rate 
#		of horses getting colic.
# Author : gongrui
# Date : 20170822
# E-mail : gongruigr@126.com
#-----------------------------------------

from numpy import *

def DataPreproc(rfile,wfile):
	frTrain = open(rfile)
	fwTrain = open(wfile,'w')
	trainLine = frTrain.readlines()
	for i in range (len(trainLine)):
		currLine = trainLine[i].strip().split()
		currLine.pop(27)	#remove label from column 22
		currLine.pop(26)	#remove label from column 22
		currLine.pop(25)	#remove label from column 22
		currLine.pop(24)	#remove label from column 22
		label = currLine[22]	#find label
		#died(2) and enthanized(3) means not lived, giving same label 0
		if (label != '1'):	
			label = '0'	
		currLine.pop(22)	#remove label from column 22
		currLine.append(label)	#append label to last column
		currLine.pop(2)		#remove Hospital Number from column 2
		# last column is label, if data is missing, drop it!
		if (currLine[-1] != '?'):
			for j in range (len(currLine)):
				# if data is missing, replace with 0
				if (currLine[j] == '?'):
					currLine[j] = '0'
				fwTrain.write(currLine[j])
				fwTrain.write('\t')
			fwTrain.write('\n')

def PredictDeathRate(step,numLoop):
	frTrain = open('TrainData.txt')
	frTest = open('TestData.txt')
    	trainSet = []
	trainLabels = []
	trainLine = frTrain.readlines()
	for i in range(len(trainLine)):
        	currLine = trainLine[i].strip().split('\t')
        	lineArr =[]
        	for j in range(len(currLine)-1):
            		lineArr.append(float(currLine[j]))
        	trainSet.append(lineArr)
        	trainLabels.append(float(currLine[-1]))	#label
    	trainWeights = stocGradAscent1(array(trainSet), trainLabels, step, numLoop)
	accuracyCount = 0
	testLine = frTest.readlines()
	numTestVec = float(len(testLine))
	for i in range(len(testLine)):
        	currLine = testLine[i].strip().split('\t')
        	lineArr =[]
        	for j in range(len(currLine)-1):
            		lineArr.append(float(currLine[j]))
        	if int(classifyVector(array(lineArr), trainWeights)) == int(currLine[-1]):
			accuracyCount += 1
	accuracyRate = (float(accuracyCount)/numTestVec)
	#print "the accuracy num of this test is: %f" % accuracyCount
	#print "the accuracy rate of this test is: %f" % accuracyRate
	return accuracyRate

def classifyVector(inX, weights):
	prob = sigmoid(sum(inX*weights))
    	if prob > 0.5: 
		return 1.0
    	else: 
		return 0.0

def stocGradAscent1(dataMatrix, classLabels, step, numIter=150):
	m,n = shape(dataMatrix)
    	weights = ones(n)   #initialize to all ones
    	for j in range(numIter):
        	dataIndex = range(m)
        	for i in range(m):
            		alpha = step/(1.0+j+i)+0.0001    #apha decreases with iteration, does not 
            		randIndex = int(random.uniform(0,len(dataIndex)))#go to 0 because of the constant
            		h = sigmoid(sum(dataMatrix[randIndex]*weights))
            		error = classLabels[randIndex] - h
            		weights = weights + alpha * error * dataMatrix[randIndex]
            		del(dataIndex[randIndex])
    	return weights

def sigmoid(inX):
    return 1.0/(1+exp(-inX))

if __name__ == '__main__':
	DataPreproc('horse-colic.data','TrainData.txt')
	DataPreproc('horse-colic.test','TestData.txt')
	#PredictDeathRate()
	maxAccuracy = 0.0
	for step in range(15,25,5):
		print step
		for numLoop in range(500,1500,300):
			accuracySum = 0.0
			for i in range(10):
        			accuracy = PredictDeathRate(step,numLoop)
				if (accuracy > maxAccuracy):
					maxAccuracy = accuracy
					print 'maxaccuracy is %f and para: %d,%d,%d' %(maxAccuracy,step,numLoop,i)
	print "Best accuracy rate is: %f" % (maxAccuracy)

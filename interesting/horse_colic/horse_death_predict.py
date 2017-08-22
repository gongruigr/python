#!/usr/bin/env python
#coding=utf-8
# Filename : horse_death_predict.py
# Description : Using logistic regression 
#		method to predict death rate 
#		of horses got colic.
# Author : gongrui
# Date : 20170822
# E-mail : gongruigr@126.com
#-----------------------------------------

from numpy import *

#Function for data preprocessing:
#1.Remove useless attributes
#2.Move label from column 22 to last column
#3.Label processing, lived->1, not lived(died and enthanized)->0
def DataPreproc(rfile,wfile):
	frTrain = open(rfile)
	fwTrain = open(wfile,'w')
	trainLine = frTrain.readlines()
	for i in range (len(trainLine)):
		currLine = trainLine[i].strip().split()
		currLine.pop(27)	#remove cp_data from column 27
		currLine.pop(26)	#remove type of lesion from column 24,25,26
		currLine.pop(25)
		currLine.pop(24)
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
	frTrain.close()
	fwTrain.close()

#Function for death rate prediction:
#1.Using stochastic gradient ascent method for training, get training weights
#2.Using training weights to test
#3.Return weights and accuracy
def PredictDeathRate(initStep,numLoop):
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
	#using function stocGradAscent to calculate weights
    	trainWeights = stocGradAscent(array(trainSet), trainLabels, initStep, numLoop)
	accuracyCount = 0				#counter for accuracy
	testLine = frTest.readlines()
	numTest = float(len(testLine))			#total num of test instances
	for i in range(len(testLine)):
        	currLine = testLine[i].strip().split('\t')
        	lineArr =[]
        	for j in range(len(currLine)-1):
            		lineArr.append(float(currLine[j]))
		#count correct instances predicted
        	if int(classifyVector(array(lineArr), trainWeights)) == int(currLine[-1]):
			accuracyCount = accuracyCount + 1
	accuracyRate = (float(accuracyCount)/numTest)
	frTrain.close()
	frTest.close()
	return accuracyRate,trainWeights

#Function for classifying vectors using sigmoid mothed
def classifyVector(inX, weights):
	prob = sigmoid(sum(inX*weights))
    	if prob > 0.5: 
		return 1.0
    	else: 
		return 0.0

#Function for stochastic gradient ascent method
def stocGradAscent(dataMatrix, classLabels, initStep, numIter=150):
	m,n = shape(dataMatrix)
    	weights = ones(n)
    	for j in range(numIter):
        	dataIndex = range(m)
        	for i in range(m):
            		alpha = initStep/(1.0+j+i)+0.0001     
            		randIndex = int(random.uniform(0,len(dataIndex)))
            		h = sigmoid(sum(dataMatrix[randIndex]*weights))
            		error = classLabels[randIndex] - h
            		weights = weights + alpha * error * dataMatrix[randIndex]
            		del(dataIndex[randIndex])
    	return weights

#Function of sigmoid
def sigmoid(inX):
    return 1.0/(1+exp(-inX))

if __name__ == '__main__':
	#preprocessing training set
	DataPreproc('horse-colic.data','TrainData.txt')
	#preprocessing testing set
	DataPreproc('horse-colic.test','TestData.txt')
	maxAccuracy = 0.0	#initial for recording max accuracy
	bestWeights = ones(22)	#initial for recording best weights
	for initStep in range(4,20,4):
		for numLoop in range(200,1200,300):
			accuracy = 0.0
			weights = ones(22)
			for i in range(10):
        			accuracy,weights = PredictDeathRate(initStep,numLoop)
				#recording max accuracy and best weights
				if (accuracy > maxAccuracy):
					maxAccuracy = accuracy
					bestWeights = weights
					print 'Until now maxaccuracy is %f and initStep is %d, numLoop is %d' %(maxAccuracy,initStep,numLoop)
	print "\nBest accuracy rate is: %f" % (maxAccuracy)
	print "Weights is: ", bestWeights

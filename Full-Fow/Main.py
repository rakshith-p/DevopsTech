import numpy as np
from Neural_Network import *
from trainer import *
from operations import *
from LogParser import *
import os
from scipy import optimize



class Main(object):
	def __init__(self):
		self.NeuralNetwork = Neural_Network()
		X = np.array(([0,0],[1,0],[0,1],[1,1]),dtype=float)
		y = np.array(([0],[1],[1],[1]),dtype=float)
		y = y/1;
		self.TrainNetwork = trainer(self.NeuralNetwork)
		self.TrainNetwork.train(X,y)
		
		
		#Initialize and train neural Network
		
		self.AIMLPs = AIMLParser()
		self.logObj = LogParser()
		#Initialize Helper Objects
		
		self.logFile = open("/var/log/apache2/error.log",'r') #log file Open
		
		self.readTime = open("time.txt",'r')
		
		self.lastStat=self.readTime.readline()
		self.updatStat = self.lastStat
		
		self.Xin = self.parseFile(self.logFile) ## parse log file form current time 
		self.Xin = [1.0,1.0]
		self.ResOut = self.NeuralNetwork.forward(self.Xin)

		if 1.0==round(self.ResOut[0]):
			self.command=self.getCommand('Apache2')
			self.doOperation()
			print "Restart successful!"
		self.logFile.close()
		
	
		
		
	def getCommand(self,pattern):
		self.command= self.AIMLPs.getAction(pattern)
		return self.command
		
	def doOperation(self):
		self.inCommand = 'echo "Raks@1601"|sudo -S '
		self.inCommand = self.inCommand + self.command
		os.system(self.inCommand)
				
	def parseFile(self,logFile):
		if self.lastStat:
			for line in iter(logFile):
				parserGroups=logObj.parseLog(line)
				self.updatStat = parserGroups[2]
				if self.updatStat>self.lastStat:
					if parserGroups[4] == 'notice' and parserGroups[13] == 'caught SIGTERM, shutting down':
						self.writeTime = open("time.txt",'w')
						self.writeTime.write(self.updatStat)
						X=np.array(([1.0,1.0]),dtype=float)
						return X
					
					
				
	
		
	
		


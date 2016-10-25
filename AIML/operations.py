import aiml
import os

#<-- version 1.2 with Added Relearn Mechanism 

class AIMLParser(object):
	
	def __init__(self):
		self.kernel = aiml.Kernel()
		if os.path.isfile("bot_brain.brn"):
			self.kernel.bootstrap(brainFile = "bot_brain.brn")
			
		else:
			self.reLearn()

	def getAction(self,MLInput):
		self.application=MLInput[0]
		self.msg=MLInput[1]
		self.initial = self.kernel.respond(self.application)
		self.bot_response = self.kernel.respond(self.msg)
		return self.bot_response
	
	def reLearn(self):
		self.kernel.bootstrap(brainFile = "bot_brain.brn",learnFiles = "std-startup.xml", commands = "load aiml b")
		self.kernel.saveBrain("bot_brain.brn")
		
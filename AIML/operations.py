import aiml
import os



class AIMLParser(object):
	
	def __init__(self):
		self.kernel = aiml.Kernel()
		if os.path.isfile("bot_brain.brn"):
			self.kernel.bootstrap(brainFile = "bot_brain.brn")
		else:
			self.kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
			self.kernel.saveBrain("bot_brain.brn")

	def getAction(self,MLInput):
		self.msg=MLInput
		self.bot_response = self.kernel.respond(self.msg)
		return self.bot_response
		
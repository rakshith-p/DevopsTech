import numpy as np
import re

class LogParser(object):
	def __init__(self):
		self.regex = '((\[(.*?)\]) (\[(.*?)\]) (\[pid (.*?)\]) ((.*?): )?((.*?): )?((.*?): )?(.*)?)$'
			
	def parseLog(self,line):
			parserGroups=re.match(self.regex,line)
			return parserGroups
		